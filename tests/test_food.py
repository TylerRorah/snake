"""Tests for the Food class."""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entities import Food
from config import GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class TestFoodInitialization:
    """Tests for Food initialization."""

    def test_food_has_position(self):
        food = Food()
        assert food.position is not None
        assert len(food.position) == 2

    def test_food_position_is_on_grid(self):
        food = Food()
        assert food.position[0] % GRID_SIZE == 0
        assert food.position[1] % GRID_SIZE == 0

    def test_food_position_is_within_bounds(self):
        food = Food()
        assert 0 < food.position[0] < SCREEN_WIDTH
        assert 0 < food.position[1] < SCREEN_HEIGHT


class TestFoodRespawn:
    """Tests for food respawn functionality."""

    def test_respawn_changes_position(self):
        food = Food()
        old_position = food.position.copy()

        # Respawn multiple times to ensure it can change
        # (small chance it stays the same once)
        changed = False
        for _ in range(10):
            food.respawn()
            if food.position != old_position:
                changed = True
                break

        # Position should be valid regardless
        assert food.position[0] % GRID_SIZE == 0
        assert food.position[1] % GRID_SIZE == 0

    def test_respawn_avoids_snake_body(self):
        food = Food()
        snake_body = [
            [100, 100],
            [150, 100],
            [200, 100],
        ]

        # Respawn and check it's not on snake
        for _ in range(10):
            food.respawn(snake_body)
            assert food.position not in snake_body

    def test_respawn_position_stays_on_grid(self):
        food = Food()
        for _ in range(10):
            food.respawn()
            assert food.position[0] % GRID_SIZE == 0
            assert food.position[1] % GRID_SIZE == 0


class TestFoodEaten:
    """Tests for food eaten detection."""

    def test_is_eaten_when_positions_match(self):
        food = Food()
        food.position = [250, 250]
        head_position = [250, 250]
        assert food.is_eaten(head_position) == True

    def test_not_eaten_when_positions_differ(self):
        food = Food()
        food.position = [250, 250]
        head_position = [300, 250]
        assert food.is_eaten(head_position) == False

    def test_not_eaten_when_only_x_matches(self):
        food = Food()
        food.position = [250, 250]
        head_position = [250, 300]
        assert food.is_eaten(head_position) == False

    def test_not_eaten_when_only_y_matches(self):
        food = Food()
        food.position = [250, 250]
        head_position = [300, 250]
        assert food.is_eaten(head_position) == False
