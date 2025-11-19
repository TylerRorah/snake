"""Game configuration constants."""

# Screen settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
GRID_SIZE = 50

# Colors (RGB tuples)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
FPS = 7
INITIAL_SNAKE_LENGTH = 1
INITIAL_SNAKE_POSITION = (GRID_SIZE * 5, GRID_SIZE * 5)
INITIAL_DIRECTION = 'RIGHT'

# Font settings
SCORE_FONT = 'consolas'
SCORE_FONT_SIZE = 50
GAME_OVER_FONT = 'times new roman'
GAME_OVER_FONT_SIZE = 90
FINAL_SCORE_FONT = 'times'
FINAL_SCORE_FONT_SIZE = 50
PAUSE_FONT = 'consolas'
PAUSE_FONT_SIZE = 70
INSTRUCTION_FONT_SIZE = 30

# High score file
HIGH_SCORE_FILE = 'high_score.txt'
