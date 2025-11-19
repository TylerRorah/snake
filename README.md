# Snake Game

A classic snake game built with Python and Pygame, featuring a modular architecture designed for testability and maintainability.

## Features

- Classic snake gameplay with smooth controls
- Pause/resume functionality
- High score persistence across sessions
- Game over screen with restart option
- Clean, modular codebase with comprehensive tests

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd snake
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

Run the game:
```bash
python main.py
```

### Controls

| Key | Action |
|-----|--------|
| W / Arrow Up | Move up |
| S / Arrow Down | Move down |
| A / Arrow Left | Move left |
| D / Arrow Right | Move right |
| P | Pause/Resume |
| R | Restart (after game over) |

### Objective

Eat the red food to grow longer and increase your score. Avoid hitting the walls or your own body!

## Project Structure

```
snake/
├── main.py           # Entry point - game loop and pygame initialization
├── config.py         # All game constants (colors, sizes, speeds)
├── game_state.py     # GameState class - score and running state
├── entities.py       # Snake and Food classes
├── game_engine.py    # Core game logic (testable without display)
├── renderer.py       # All pygame drawing operations
├── high_score.py     # High score persistence
├── requirements.txt  # Dependencies (pygame, pytest)
├── CHANGELOG.md      # Version history
└── tests/            # Unit test suite
    ├── test_snake.py
    ├── test_food.py
    ├── test_game_state.py
    ├── test_game_engine.py
    └── test_high_score.py
```

## Running Tests

Run all tests:
```bash
python -m pytest tests/ -v
```

Run tests with coverage:
```bash
python -m pytest tests/ --cov=. --cov-report=html
```

## Configuration

Game settings can be modified in `config.py`:

- `SCREEN_WIDTH` / `SCREEN_HEIGHT` - Window dimensions (default: 1000x1000)
- `GRID_SIZE` - Size of each grid cell (default: 50px)
- `FPS` - Game speed (default: 7)
- Colors, fonts, and other visual settings

## Architecture

The codebase follows separation of concerns:

- **Config** - Centralized constants
- **Entities** - Data classes that own their state (Snake, Food)
- **GameEngine** - Pure game logic, no rendering dependencies
- **Renderer** - All pygame drawing isolated here
- **GameState** - Simple state container for score and game status
- **HighScore** - File-based persistence for high scores

This architecture enables unit testing of game logic without requiring a display.

## License

MIT License
