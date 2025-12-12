#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neocadia Design Coordinator

Coordinates multiple Claude Code instances as specialized design agents
working in series to iterate on game design specifications.

Each agent has a specific role and perspective, reviewing and improving
the specs before passing to the next agent in the chain.

Usage:
    python specs/designer.py [--iterations N] [--focus AREA] [--dry-run]
"""

import subprocess
import json
import argparse
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


# === Agent Role Definitions ===

@dataclass
class DesignAgent:
    """A specialized design agent with a specific role and focus."""
    name: str
    role: str
    focus_areas: list[str]
    prompt_template: str
    output_instructions: str = ""

    def build_prompt(self, context: dict) -> str:
        """Build the full prompt for this agent."""
        prompt = self.prompt_template.format(**context)
        if self.output_instructions:
            prompt += f"\n\n{self.output_instructions}"
        return prompt


# Define the agent roster - each brings a different perspective
AGENTS: dict[str, DesignAgent] = {
    "creative_director": DesignAgent(
        name="Creative Director",
        role="creative_director",
        focus_areas=["world/*", "zones/*", "art/*"],
        prompt_template="""You are the Creative Director for Neocadia.

Your job is to ensure creative cohesion across the project. Review the current specs with these questions:

1. **Visual Identity**: Do all zones feel like they belong to the same universe while being distinct?
2. **Emotional Arc**: Does the player's journey have satisfying emotional beats?
3. **Aesthetic Consistency**: Are color palettes, art direction, and tone aligned?
4. **Magic Moments**: Where are the "wow" moments? Are there enough?

Current focus: {focus_area}
Iteration: {iteration}/{max_iterations}

{additional_context}

Review the specs in `specs/` and make targeted improvements. Focus on creative vision, not mechanics.
Edit files directly when you see opportunities to strengthen the creative direction."""
    ),

    "systems_designer": DesignAgent(
        name="Systems Designer",
        role="systems_designer",
        focus_areas=["systems/*", "minigames/*"],
        prompt_template="""You are the Systems Designer for Neocadia.

Your job is to ensure all game systems are balanced, interconnected, and fun. Review with these questions:

1. **Economy Balance**: Are token earn/spend rates creating good progression pacing?
2. **Loop Tightness**: Is each minigame's core loop satisfying in 30 seconds?
3. **System Integration**: Do systems talk to each other? (tokens → restoration → unlocks)
4. **Player Agency**: Does the player have meaningful choices?

Current focus: {focus_area}
Iteration: {iteration}/{max_iterations}

{additional_context}

Review the specs in `specs/` and make targeted improvements. Add specific numbers where vague.
Identify and fix any exploits or dead ends in the economy. Edit files directly."""
    ),

    "narrative_designer": DesignAgent(
        name="Narrative Designer",
        role="narrative_designer",
        focus_areas=["world/*", "characters/*"],
        prompt_template="""You are the Narrative Designer for Neocadia.

Your job is to ensure story, characters, and world-building are compelling. Review with these questions:

1. **Character Depth**: Do characters want things beyond helping the player?
2. **Story Stakes**: What happens if the player fails? Does it matter?
3. **World Logic**: Does the lore hold together under scrutiny?
4. **Dialogue Voice**: Would you recognize each character from their lines alone?

Current focus: {focus_area}
Iteration: {iteration}/{max_iterations}

{additional_context}

Review the specs in `specs/` and make targeted improvements. Add actual dialogue samples.
Deepen character motivations and relationships. Edit files directly."""
    ),

    "ux_designer": DesignAgent(
        name="UX Designer",
        role="ux_designer",
        focus_areas=["ui/*", "zones/*"],
        prompt_template="""You are the UX Designer for Neocadia.

Your job is to ensure the player experience is smooth and intuitive. Review with these questions:

1. **Onboarding**: Can a new player understand the game in 2 minutes?
2. **Navigation**: Is it always clear where you can go and what you can do?
3. **Feedback**: Does every action have satisfying feedback?
4. **Accessibility**: Can players with different abilities enjoy the game?

Current focus: {focus_area}
Iteration: {iteration}/{max_iterations}

{additional_context}

Review the specs in `specs/` and make targeted improvements. Map the first-time user experience.
Identify confusion points and fix them. Edit files directly."""
    ),

    "critic": DesignAgent(
        name="Design Critic",
        role="critic",
        focus_areas=["*"],
        prompt_template="""You are the Design Critic for Neocadia.

Your job is to find weaknesses, inconsistencies, and missed opportunities. Be constructively brutal.

1. **Contradictions**: Where do specs disagree with each other?
2. **Vagueness**: Where are specs too hand-wavy to implement?
3. **Clichés**: Where are we being lazy or derivative?
4. **Missing Pieces**: What obvious questions do the specs fail to answer?

Current focus: {focus_area}
Iteration: {iteration}/{max_iterations}

{additional_context}

Review the specs in `specs/` and write a critique to `specs/CRITIQUE.md`.
Be specific. Name files and line numbers. Suggest fixes, don't just complain.
Do NOT edit the spec files directly - only write to CRITIQUE.md."""
    ),

    "integrator": DesignAgent(
        name="Integration Lead",
        role="integrator",
        focus_areas=["*"],
        prompt_template="""You are the Integration Lead for Neocadia.

Your job is to ensure all parts of the design work together as a whole.

1. **Cross-References**: Do specs reference each other correctly?
2. **Dependencies**: Are implementation dependencies clear?
3. **Gaps**: Are there holes between what one spec assumes and another provides?
4. **Priority Alignment**: Do P1/P2/P3 priorities make sense together?

Current focus: {focus_area}
Iteration: {iteration}/{max_iterations}

Previous critique to address:
{additional_context}

Review the specs in `specs/` and fix integration issues. Update cross-references.
Ensure the README.md index is accurate. Edit files directly."""
    ),
}


# === Pipeline Definitions ===

# Different pipelines for different purposes
PIPELINES: dict[str, list[str]] = {
    "full": [
        "creative_director",
        "systems_designer",
        "narrative_designer",
        "ux_designer",
        "critic",
        "integrator",
    ],
    "creative": [
        "creative_director",
        "narrative_designer",
        "critic",
    ],
    "systems": [
        "systems_designer",
        "ux_designer",
        "critic",
    ],
    "polish": [
        "critic",
        "integrator",
    ],
    "quick": [
        "critic",
    ],
}


# === Execution Engine ===

@dataclass
class IterationResult:
    """Result from a single agent iteration."""
    agent: str
    success: bool
    duration_seconds: float
    files_modified: list[str] = field(default_factory=list)
    summary: str = ""
    error: Optional[str] = None


@dataclass
class PipelineResult:
    """Result from a full pipeline run."""
    pipeline: str
    iteration: int
    results: list[IterationResult] = field(default_factory=list)

    @property
    def all_succeeded(self) -> bool:
        return all(r.success for r in self.results)


def run_claude_agent(
    prompt: str,
    working_dir: Path,
    timeout_seconds: int = 300,
    dry_run: bool = False,
) -> tuple[bool, str, float]:
    """
    Run a Claude Code instance with the given prompt.

    Returns (success, output, duration_seconds)
    """
    if dry_run:
        print(f"[DRY RUN] Would execute prompt ({len(prompt)} chars)")
        return True, "[dry run - no output]", 0.0

    start = datetime.now()

    try:
        # Invoke claude CLI with the prompt
        result = subprocess.run(
            [
                "claude",
                "--print",  # Print output to stdout
                "--dangerously-skip-permissions",  # Auto-approve file edits
            ],
            input=prompt,
            capture_output=True,
            text=True,
            cwd=working_dir,
            timeout=timeout_seconds,
        )

        duration = (datetime.now() - start).total_seconds()
        success = result.returncode == 0
        output = result.stdout if success else result.stderr

        return success, output, duration

    except subprocess.TimeoutExpired:
        duration = (datetime.now() - start).total_seconds()
        return False, f"Timeout after {timeout_seconds}s", duration
    except FileNotFoundError:
        return False, "Claude CLI not found. Install with: npm install -g @anthropic-ai/claude-code", 0.0
    except Exception as e:
        duration = (datetime.now() - start).total_seconds()
        return False, f"Error: {e}", duration


def get_git_modified_files(working_dir: Path) -> list[str]:
    """Get list of files modified since last commit."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only"],
            capture_output=True,
            text=True,
            cwd=working_dir,
        )
        if result.returncode == 0:
            return [f for f in result.stdout.strip().split("\n") if f]
    except Exception:
        pass
    return []


def run_agent(
    agent: DesignAgent,
    context: dict,
    working_dir: Path,
    dry_run: bool = False,
) -> IterationResult:
    """Run a single design agent."""
    print(f"\n{'='*60}")
    print(f"  {agent.name}")
    print(f"  Focus: {', '.join(agent.focus_areas)}")
    print(f"{'='*60}\n")

    # Build the prompt
    prompt = agent.build_prompt(context)

    # Track files before
    files_before = set(get_git_modified_files(working_dir))

    # Run claude
    success, output, duration = run_claude_agent(
        prompt=prompt,
        working_dir=working_dir,
        dry_run=dry_run,
    )

    # Track files after
    files_after = set(get_git_modified_files(working_dir))
    files_modified = list(files_after - files_before)

    # Extract summary (last paragraph of output, roughly)
    summary = output[-500:] if len(output) > 500 else output

    result = IterationResult(
        agent=agent.role,
        success=success,
        duration_seconds=duration,
        files_modified=files_modified,
        summary=summary,
        error=None if success else output,
    )

    # Print result
    status = "✓" if success else "✗"
    print(f"\n{status} {agent.name} completed in {duration:.1f}s")
    if files_modified:
        print(f"  Modified: {', '.join(files_modified[:5])}")
        if len(files_modified) > 5:
            print(f"  ... and {len(files_modified) - 5} more")

    return result


def run_pipeline(
    pipeline_name: str,
    iteration: int,
    max_iterations: int,
    focus_area: str,
    working_dir: Path,
    dry_run: bool = False,
) -> PipelineResult:
    """Run a complete pipeline of agents."""

    pipeline = PIPELINES.get(pipeline_name)
    if not pipeline:
        raise ValueError(f"Unknown pipeline: {pipeline_name}. Available: {list(PIPELINES.keys())}")

    result = PipelineResult(pipeline=pipeline_name, iteration=iteration)

    # Build shared context
    context = {
        "iteration": iteration,
        "max_iterations": max_iterations,
        "focus_area": focus_area,
        "additional_context": "",
    }

    # Load previous critique if it exists
    critique_path = working_dir / "specs" / "CRITIQUE.md"
    if critique_path.exists():
        context["additional_context"] = f"Previous critique:\n{critique_path.read_text()[:2000]}"

    # Run each agent in series
    for agent_name in pipeline:
        agent = AGENTS.get(agent_name)
        if not agent:
            print(f"Warning: Unknown agent {agent_name}, skipping")
            continue

        agent_result = run_agent(
            agent=agent,
            context=context,
            working_dir=working_dir,
            dry_run=dry_run,
        )
        result.results.append(agent_result)

        # Update context with this agent's output for next agent
        if agent_result.success and agent_result.summary:
            context["additional_context"] = f"Previous agent ({agent.name}) notes:\n{agent_result.summary}"

        # Stop pipeline on failure (optional - could make configurable)
        if not agent_result.success:
            print(f"\nPipeline stopped due to {agent.name} failure")
            break

    return result


def write_iteration_log(
    results: list[PipelineResult],
    working_dir: Path,
):
    """Write a log of all iterations."""
    log_path = working_dir / "specs" / "ITERATION_LOG.md"

    content = ["# Design Iteration Log\n"]
    content.append(f"Generated: {datetime.now().isoformat()}\n\n")

    for pipeline_result in results:
        content.append(f"## Iteration {pipeline_result.iteration} ({pipeline_result.pipeline})\n\n")

        for agent_result in pipeline_result.results:
            status = "✓" if agent_result.success else "✗"
            content.append(f"### {status} {agent_result.agent}\n\n")
            content.append(f"- Duration: {agent_result.duration_seconds:.1f}s\n")
            if agent_result.files_modified:
                content.append(f"- Files modified: {len(agent_result.files_modified)}\n")
                for f in agent_result.files_modified[:10]:
                    content.append(f"  - `{f}`\n")
            if agent_result.error:
                content.append(f"- Error: {agent_result.error[:200]}\n")
            content.append("\n")

    log_path.write_text("".join(content))
    print(f"\nIteration log written to {log_path}")


# === CLI ===

def main():
    parser = argparse.ArgumentParser(
        description="Coordinate Claude Code instances to iterate on Neocadia design specs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Pipelines:
  full      - All agents: creative → systems → narrative → ux → critic → integrator
  creative  - Creative focus: creative_director → narrative → critic
  systems   - Systems focus: systems_designer → ux → critic
  polish    - Final polish: critic → integrator
  quick     - Just critic

Examples:
  python specs/designer.py                    # Run full pipeline once
  python specs/designer.py -n 3               # Run 3 iterations
  python specs/designer.py -p creative        # Creative-focused iteration
  python specs/designer.py -f "minigames/*"   # Focus on minigames
  python specs/designer.py --dry-run          # Preview without running
        """
    )

    parser.add_argument(
        "-n", "--iterations",
        type=int,
        default=1,
        help="Number of iterations to run (default: 1)"
    )

    parser.add_argument(
        "-p", "--pipeline",
        choices=list(PIPELINES.keys()),
        default="full",
        help="Which pipeline to run (default: full)"
    )

    parser.add_argument(
        "-f", "--focus",
        default="all specs",
        help="Focus area description passed to agents"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without running agents"
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Timeout per agent in seconds (default: 300)"
    )

    args = parser.parse_args()

    # Determine working directory (project root)
    script_path = Path(__file__).resolve()
    working_dir = script_path.parent.parent  # specs/ -> project root

    if not (working_dir / "specs").is_dir():
        print(f"Error: specs/ directory not found in {working_dir}")
        sys.exit(1)

    print(f"""
╔══════════════════════════════════════════════════════════════╗
║           NEOCADIA DESIGN COORDINATOR                        ║
╠══════════════════════════════════════════════════════════════╣
║  Pipeline:    {args.pipeline:<46} ║
║  Iterations:  {args.iterations:<46} ║
║  Focus:       {args.focus[:44]:<46} ║
║  Working dir: {str(working_dir)[:44]:<46} ║
╚══════════════════════════════════════════════════════════════╝
""")

    if args.dry_run:
        print(">>> DRY RUN MODE - No agents will be executed <<<\n")

    all_results: list[PipelineResult] = []

    for i in range(1, args.iterations + 1):
        print(f"\n{'#'*60}")
        print(f"#  ITERATION {i} of {args.iterations}")
        print(f"{'#'*60}")

        result = run_pipeline(
            pipeline_name=args.pipeline,
            iteration=i,
            max_iterations=args.iterations,
            focus_area=args.focus,
            working_dir=working_dir,
            dry_run=args.dry_run,
        )
        all_results.append(result)

        if not result.all_succeeded:
            print(f"\nIteration {i} had failures. Stopping.")
            break

    # Write log
    if not args.dry_run:
        write_iteration_log(all_results, working_dir)

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    total_agents = sum(len(r.results) for r in all_results)
    successful = sum(1 for r in all_results for ar in r.results if ar.success)
    total_time = sum(ar.duration_seconds for r in all_results for ar in r.results)

    print(f"Iterations completed: {len(all_results)}/{args.iterations}")
    print(f"Agents run: {successful}/{total_agents} succeeded")
    print(f"Total time: {total_time:.1f}s")

    # Exit with error if any failures
    if successful < total_agents:
        sys.exit(1)


if __name__ == "__main__":
    main()
