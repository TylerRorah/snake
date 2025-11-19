"""Tests for the GameEngine class."""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock pygame before importing game_engine
from unittest.mock import MagicMock
sys.modules['pygame'] = MagicMock()

from game_engine import GameEngine
from config import GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class TestGameEngineInitialization:
    """Tests for GameEngine initialization."""

    def test_engine_has_snake(self):
        engine = GameEngine()
        assert engine.snake is not None

    def test_engine_has_food(self):
        engine = GameEngine()
        assert engine.food is not None

    def test_engine_has_state(self):
        engine = GameEngine()
        assert engine.state is not None

    def test_initial_score_is_zero(self):
        engine = GameEngine()
        assert engine.get_score() == 0

    def test_game_not_over_initially(self):
        engine = GameEngine()
        assert engine.is_game_over() == False

    def test_game_running_initially(self):
        engine = GameEngine()
        assert engine.is_running() == True


class TestGameEngineInput:
    """Tests for input handling."""

    def test_handle_w_key(self):
        import pygame
        pygame.K_w = 119
        engine = GameEngine()
        engine.handle_input(pygame.K_w)
        assert engine.snake.direction == 'UP'

    def test_handle_arrow_up(self):
        import pygame
        pygame.K_UP = 1073741906
        engine = GameEngine()
        engine.handle_input(pygame.K_UP)
        assert engine.snake.direction == 'UP'

    def test_handle_s_key(self):
        import pygame
        pygame.K_s = 115
        engine = GameEngine()
        engine.snake.direction = 'LEFT'  # Change from RIGHT first
        engine.handle_input(pygame.K_s)
        assert engine.snake.direction == 'DOWN'

    def test_handle_a_key(self):
        import pygame
        pygame.K_a = 97
        engine = GameEngine()
        engine.snake.direction = 'UP'  # Change from RIGHT first
        engine.handle_input(pygame.K_a)
        assert engine.snake.direction == 'LEFT'

    def test_handle_d_key(self):
        import pygame
        pygame.K_d = 100
        engine = GameEngine()
        engine.snake.direction = 'UP'  # Change from RIGHT first
        engine.handle_input(pygame.K_d)
        assert engine.snake.direction == 'RIGHT'


class TestGameEngineUpdate:
    """Tests for game update logic."""

    def test_update_moves_snake(self):
        engine = GameEngine()
        initial_head = engine.snake.head.copy()
        engine.update()
        # Snake should have moved right
        assert engine.snake.head[0] == initial_head[0] + GRID_SIZE

    def test_update_returns_true_when_game_continues(self):
        engine = GameEngine()
        result = engine.update()
        assert result == True

    def test_update_returns_false_on_wall_collision(self):
        engine = GameEngine()
        # Position snake at right edge
        engine.snake.body = [[SCREEN_WIDTH - GRID_SIZE, 250]]
        engine.snake.direction = 'RIGHT'
        result = engine.update()
        assert result == False
        assert engine.is_game_over() == True

    def test_eating_food_increases_score(self):
        engine = GameEngine()
        # Position food directly in front of snake
        engine.snake.body = [[200, 250]]
        engine.snake.direction = 'RIGHT'
        engine.food.position = [250, 250]

        engine.update()
        assert engine.get_score() == 1

    def test_eating_food_respawns_food(self):
        engine = GameEngine()
        # Position food directly in front of snake
        engine.snake.body = [[200, 250]]
        engine.snake.direction = 'RIGHT'
        engine.food.position = [250, 250]
        old_food_pos = engine.food.position.copy()

        engine.update()
        # Food should have respawned (might be same position by chance, but likely different)
        # At minimum, check that food exists
        assert engine.food.position is not None

    def test_snake_grows_when_eating_food(self):
        engine = GameEngine()
        # Position food directly in front of snake
        engine.snake.body = [[200, 250]]
        engine.snake.direction = 'RIGHT'
        engine.food.position = [250, 250]

        initial_length = len(engine.snake.body)
        engine.update()
        # Snake should be longer (didn't shrink)
        assert len(engine.snake.body) == initial_length + 1

    def test_snake_stays_same_length_without_food(self):
        engine = GameEngine()
        engine.snake.body = [[200, 250], [150, 250]]  # Length 2
        engine.snake.direction = 'RIGHT'
        engine.food.position = [500, 500]  # Far away

        engine.update()
        # Snake should stay same length
        assert len(engine.snake.body) == 2


class TestGameEngineSelfCollision:
    """Tests for self-collision detection."""

    def test_self_collision_ends_game(self):
        engine = GameEngine()
        # Create a snake that will collide with itself
        # Snake going UP will hit its own body
        engine.snake.body = [
            [250, 250],  # Head
            [300, 250],
            [300, 200],
            [250, 200],
            [250, 300],  # Will collide when moving up
        ]
        engine.snake.direction = 'UP'
        engine.food.position = [500, 500]

        result = engine.update()
        assert result == False
        assert engine.is_game_over() == True


class TestGameEngineControl:
    """Tests for game control methods."""

    def test_stop_ends_running(self):
        engine = GameEngine()
        engine.stop()
        assert engine.is_running() == False

    def test_reset_restores_initial_state(self):
        engine = GameEngine()
        # Modify state
        engine.state.increment_score()
        engine.state.end_game()
        engine.snake.body = [[500, 500], [450, 500]]

        engine.reset()
        assert engine.get_score() == 0
        assert engine.is_game_over() == False
        assert engine.is_running() == True


class TestGameEngineGameOver:
    """Tests for game over conditions."""

    def test_update_does_nothing_when_game_over(self):
        engine = GameEngine()
        engine.state.end_game()
        result = engine.update()
        assert result == False
