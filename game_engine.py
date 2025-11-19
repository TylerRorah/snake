"""Game engine - handles game logic separate from rendering."""

import pygame
from entities import Snake, Food
from game_state import GameState


class GameEngine:
    """Handles all game logic and state management."""

    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.state = GameState()

    def handle_input(self, key):
        """
        Process keyboard input.

        Args:
            key: Pygame key constant.
        """
        direction_map = {
            pygame.K_w: 'UP',
            pygame.K_UP: 'UP',
            pygame.K_s: 'DOWN',
            pygame.K_DOWN: 'DOWN',
            pygame.K_a: 'LEFT',
            pygame.K_LEFT: 'LEFT',
            pygame.K_d: 'RIGHT',
            pygame.K_RIGHT: 'RIGHT'
        }

        if key in direction_map:
            self.snake.change_direction(direction_map[key])

    def update(self):
        """
        Update game state for one frame.

        Returns:
            True if game should continue, False if game over.
        """
        if self.state.game_over:
            return False

        # Move the snake
        self.snake.move()

        # Check for food collision
        if self.food.is_eaten(self.snake.head):
            self.state.increment_score()
            self.food.respawn(self.snake.body)
        else:
            # Remove tail if no food eaten
            self.snake.shrink()

        # Check for collisions
        if self.snake.check_wall_collision() or self.snake.check_self_collision():
            self.state.end_game()
            return False

        return True

    def reset(self):
        """Reset the game to initial state."""
        self.snake.reset()
        self.food.respawn()
        self.state.reset()

    def get_score(self):
        """Get current score."""
        return self.state.score

    def is_game_over(self):
        """Check if game is over."""
        return self.state.game_over

    def is_running(self):
        """Check if game loop should continue."""
        return self.state.running

    def stop(self):
        """Stop the game loop."""
        self.state.stop_running()
