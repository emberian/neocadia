import Phaser from 'phaser';
import { GAME_WIDTH, GAME_HEIGHT } from './utils/Constants';

const config: Phaser.Types.Core.GameConfig = {
  type: Phaser.AUTO,
  width: GAME_WIDTH,
  height: GAME_HEIGHT,
  parent: 'game-container',
  backgroundColor: '#1a1a2e',
  pixelArt: false,
  roundPixels: true,
  scene: [],
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
  input: {
    mouse: {
      preventDefaultWheel: true,
    },
  },
};

const game = new Phaser.Game(config);

// Hot module replacement for development
if (import.meta.hot) {
  import.meta.hot.accept(() => {
    game.destroy(true);
    window.location.reload();
  });
}

export default game;
