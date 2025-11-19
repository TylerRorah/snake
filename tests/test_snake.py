"""Tests for the Snake class."""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entities import Snake
from config import GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, INITIAL_SNAKE_POSITION


class TestSnakeInitialization:
    """Tests for Snake initialization."""

    def test_snake_starts_at_initial_position(self):
        snake = Snake()
        assert snake.body == [list(INITIAL_SNAKE_POSITION)]

    def test_snake_starts_moving_right(self):
        snake = Snake()
        assert snake.direction == 'RIGHT'

    def test_snake_head_property(self):
        snake = Snake()
        assert snake.head == list(INITIAL_SNAKE_POSITION)


class TestSnakeDirectionChange:
    """Tests for snake direction changes."""

    def test_change_direction_to_up(self):
        snake = Snake()
        snake.change_direction('UP')
        assert snake.direction == 'UP'

    def test_change_direction_to_down(self):
        snake = Snake()
        snake.change_direction('DOWN')
        assert snake.direction == 'DOWN'

    def test_change_direction_to_left(self):
        snake = Snake()
        snake.direction = 'UP'  # First change to UP
        snake.change_direction('LEFT')
        assert snake.direction == 'LEFT'

    def test_prevents_reverse_right_to_left(self):
        snake = Snake()  # Starts going RIGHT
        snake.change_direction('LEFT')
        assert snake.direction == 'RIGHT'  # Should not change

    def test_prevents_reverse_left_to_right(self):
        snake = Snake()
        snake.direction = 'LEFT'
        snake.change_direction('RIGHT')
        assert snake.direction == 'LEFT'

    def test_prevents_reverse_up_to_down(self):
        snake = Snake()
        snake.direction = 'UP'
        snake.change_direction('DOWN')
        assert snake.direction == 'UP'

    def test_prevents_reverse_down_to_up(self):
        snake = Snake()
        snake.direction = 'DOWN'
        snake.change_direction('UP')
        assert snake.direction == 'DOWN'

    def test_invalid_direction_ignored(self):
        snake = Snake()
        snake.change_direction('INVALID')
        assert snake.direction == 'RIGHT'


class TestSnakeMovement:
    """Tests for snake movement."""

    def test_move_right(self):
        snake = Snake()
        snake.direction = 'RIGHT'
        initial_x = snake.head[0]
        snake.move()
        assert snake.head[0] == initial_x + GRID_SIZE

    def test_move_left(self):
        snake = Snake()
        snake.direction = 'LEFT'
        initial_x = snake.head[0]
        snake.move()
        assert snake.head[0] == initial_x - GRID_SIZE

    def test_move_up(self):
        snake = Snake()
        snake.direction = 'UP'
        initial_y = snake.head[1]
        snake.move()
        assert snake.head[1] == initial_y - GRID_SIZE

    def test_move_down(self):
        snake = Snake()
        snake.direction = 'DOWN'
        initial_y = snake.head[1]
        snake.move()
        assert snake.head[1] == initial_y + GRID_SIZE

    def test_move_adds_new_head(self):
        snake = Snake()
        initial_length = len(snake.body)
        snake.move()
        assert len(snake.body) == initial_length + 1

    def test_shrink_removes_tail(self):
        snake = Snake()
        snake.move()  # Now length is 2
        snake.shrink()
        assert len(snake.body) == 1


class TestSnakeCollisions:
    """Tests for collision detection."""

    def test_wall_collision_left(self):
        snake = Snake()
        snake.body = [[-GRID_SIZE, 250]]
        assert snake.check_wall_collision() == True

    def test_wall_collision_right(self):
        snake = Snake()
        snake.body = [[SCREEN_WIDTH, 250]]
        assert snake.check_wall_collision() == True

    def test_wall_collision_top(self):
        snake = Snake()
        snake.body = [[250, -GRID_SIZE]]
        assert snake.check_wall_collision() == True

    def test_wall_collision_bottom(self):
        snake = Snake()
        snake.body = [[250, SCREEN_HEIGHT]]
        assert snake.check_wall_collision() == True

    def test_no_wall_collision_inside(self):
        snake = Snake()
        snake.body = [[250, 250]]
        assert snake.check_wall_collision() == False

    def test_self_collision_detected(self):
        snake = Snake()
        # Create a snake that collides with itself
        snake.body = [
            [250, 250],  # Head
            [200, 250],
            [200, 300],
            [250, 300],
            [250, 250],  # Collision with head
        ]
        assert snake.check_self_collision() == True

    def test_no_self_collision(self):
        snake = Snake()
        snake.body = [
            [250, 250],
            [200, 250],
            [150, 250],
        ]
        assert snake.check_self_collision() == False

    def test_no_self_collision_single_segment(self):
        snake = Snake()
        assert snake.check_self_collision() == False


class TestSnakeReset:
    """Tests for snake reset functionality."""

    def test_reset_restores_initial_position(self):
        snake = Snake()
        snake.body = [[500, 500], [450, 500], [400, 500]]
        snake.direction = 'UP'
        snake.reset()
        assert snake.body == [list(INITIAL_SNAKE_POSITION)]
        assert snake.direction == 'RIGHT'
