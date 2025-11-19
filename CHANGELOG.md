# Changelog

All notable changes to the Snake Game project will be documented in this file.

## [Unreleased]

## [1.2.0] - 2025-11-18

### Added
- Pause functionality with P key toggle
- Visual pause overlay with semi-transparent darkening effect
- High score persistence to file (`high_score.txt`)
- High score display on game over screen
- "NEW HIGH SCORE!" celebration message when beating previous record
- Restart capability with R key after game over
- `high_score.py` module for score persistence management
- `GameState.paused` property and `toggle_pause()` method
- `GameEngine.is_paused()` method
- `Renderer.draw_paused()` method for pause overlay
- 23 new unit tests for pause and high score features

### Changed
- Improved game over screen with score, high score, and restart instructions
- Game no longer auto-exits after death - player can restart or quit
- `Renderer.draw_game_over()` now accepts optional `high_score` parameter
- Updated `.gitignore` to exclude `high_score.txt` data file

### Removed
- Automatic exit delay after game over (replaced with restart option)

## [1.1.0] - 2025-11-18

### Added
- Comprehensive test suite with pytest (69 tests)
- Tests for Snake movement and direction changes
- Tests for collision detection (walls and self)
- Tests for Food spawning and eaten detection
- Tests for GameState management
- Tests for GameEngine update loop and game over conditions
- Mock pygame support for headless testing

## [1.0.0] - 2025-11-18

### Added
- Initial modular architecture refactor
- `config.py` - Centralized game constants
- `game_state.py` - GameState class for score and running state
- `entities.py` - Snake and Food classes with proper encapsulation
- `game_engine.py` - Core game logic separated from rendering
- `renderer.py` - All pygame drawing operations
- `main.py` - Entry point with game loop
- `requirements.txt` - Document pygame dependency
- `.gitignore` for common Python exclusions

### Changed
- Eliminated global state
- Separated concerns for better testability
- Snake prevents 180-degree direction reversals
- Move/shrink pattern for snake growth

## [0.1.0] - 2025-11-18

### Added
- Initial snake game implementation
- Basic pygame window and game loop
- Snake movement with WASD and arrow keys
- Food spawning and eating
- Score tracking
- Wall and self-collision detection
- Game over screen with "YOU DIED" message
