# Aim Trainer

A simple aim training game built with Python and Pygame. Test and improve your mouse accuracy and reaction speed by hitting moving targets before they disappear!

## Features

- Dynamic targets that grow and shrink
- Score tracking with hits, misses, accuracy, and speed (targets per second)
- Lives system — miss too many targets and the game ends
- Clean UI with a top bar showing time, hits, speed, and remaining lives
- End screen with detailed statistics and option to restart or quit

## Installation

1. Make sure you have Python 3 installed.
2. Install Pygame if you don’t have it:

   ```bash
   pip install pygame
   ```

3. Clone or download this repository.
   ```bash
   git clone https://github.com/111morris/aim-trainer-python.git
   cd aim-trainer-python
   ```

## Usage

Run the game with:

```bash
python3 main.py
```

## Controls

    Move your mouse to aim.

    Left click to shoot targets.

    Press R on the end screen to restart the game.

    Press Q or close the window to quit.

## How it works

    Targets appear randomly on the screen and grow to a max size, then shrink.

    You must click them before they disappear.

    Missing targets reduces your lives.

    Game ends when you lose all lives, showing your stats and restart option.

## Code Structure

    main.py — main game logic and UI.

    Target class manages target behavior and collision detection.

    Utility functions for drawing UI elements and formatting time.

## Future Improvements

    Add difficulty levels with faster targets.

    Include sound effects and animations.

    High score tracking.

    Customize target colors and sizes.

## License

MIT License © 2025 Mulandi
