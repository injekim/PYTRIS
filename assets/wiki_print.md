# PYTRIS™
tetris made with pygame

<img src="https://raw.githubusercontent.com/k0626089/PYTRIS/master/assets/images/gameplay.gif" width="250">

# How to play

## How to launch the game
### Macintosh

Execute the command below

      python3 pytris.py

### Windows

Execute the command below

      python pytris.py

#### #Note. You got to have pygame installed
- [Install pygame](https://www.pygame.org/wiki/GettingStarted)

## Commands
| Command      | Key           |
|--------------|---------------|
| Move left    | Left          |
| Move right   | Right         |
| Rotate right | Up / X        |
| Rotate left  | Left ctrl / Z |
| Soft drop    | Down arrow    |
| Hard drop    | Space         |
| Hold block   | Left shift / C|
| Pause game   | Esc           |

## Score board
| Action       | Score       |
|--------------|-------------|
| Block drop   | 10 * level  |
| Single       | 50 * level  |
| Double       | 150 * level |
| Triple       | 350 * level |
| Tetris       | 1000 * level|

# Things that work

## Start screen with blinking text
<img src="https://raw.githubusercontent.com/k0626089/PYTRIS/master/assets/images/startscreen.gif" width="250">

## Leaderboard
- Displays top 3 scores on the start screen

## Randomly generated tetrimino blocks
- New block is randomly choosed from 7 tetriminos.
<img src="https://raw.githubusercontent.com/k0626089/PYTRIS/master/assets/images/tetriminos.png" width="500">

## Displays
<img src="https://raw.githubusercontent.com/k0626089/PYTRIS/master/assets/images/gameplay.png" width="300">

#### Holded block
- Holds current block when L_SHIFT is pressed.
- Holded block is displayed on the right.
#### Next block
- Next block is displayed on the right.
#### Score
- Current score is displayed on the right.
#### level
- Current level is displayed on the right.
#### Goal
- Lines required for next level is displayed on the right.

## Ghost
- Ghost mino at the bottom for enhanced game experience.

## Pause
<img src="https://raw.githubusercontent.com/k0626089/PYTRIS/master/assets/images/paused.png" width="300">

- Pause the game when 'esc' key is pressed.

## Level system
- Increase speed according to levels.
- Increase score per line according to levels.

## Preventing invalid moves
#### Prevents new blocks from penetrating bottom blocks.

    is_bottom(x, y, mino, r)

#### Prevents blocks from moving over walls.

    is_leftedge(x, y, mino, r)


    is_rightedge(x, y, mino, r)

## Kick
#### Floor kick
- Nudge the block up when it's impossible to turn without it.

#### Wall kick
- Nudge the block sideways when it's impossible to turn without it.

#### Used function

    is_turnable(x, y, mino, r)

## Remove maxed out rows
- Maxed out rows get emptied out.

## Sound effects
More on [Resources](https://github.com/k0626089/PYTRIS/wiki/Resources)

## Game over when the board is full

<img src="https://raw.githubusercontent.com/k0626089/PYTRIS/master/assets/images/gameover_1.png" width="300">

- You can save your score after the game is over.

# Things that don't work

Everything seem to work for now

#### Please notify me if you find any bugs.

# Future plans

## T-spin support
- Support for T-spin single, double, triple.

# Resources

## Framework
[pygame](https://pygame.org/) (1.9.3)

## Fonts
- OpenSans(Apache License)
- Inconsolata(SIL Open Font License)

## Sound source
[source](https://www.sounds-resource.com/pc_computer/tetriszone/sound/586/)

### Sound effect for button clicks
#### Start button / Continue button

    assets/sounds/SFX_ButtonUp.wav

#### Left / Right / Up / Down Arrows

    assets/sounds/SFX_PieceMoveLR.wav

#### Space bar(in game)

    assets/sounds/SFX_PieceHardDrop.wav

### Sound effect for Single, Double, Triple and TETRIS
#### Single line clear

    assets/sounds/SFX_SpecialLineClearSingle.wav

#### Double line clear

    assets/sounds/SFX_SpecialLineClearDouble.wav

#### Triple line clear

    assets/sounds/SFX_SpecialLineClearTriple.wav

#### Tetris

    assets/sounds/SFX_SpecialTetris.wav
