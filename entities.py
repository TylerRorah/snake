"""Game entities: Snake and Food."""

import random
from config import (
    GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT,
    WHITE, RED,
    INITIAL_SNAKE_POSITION, INITIAL_DIRECTION
)


class Snake:
    """Represents the snake player."""

    def __init__(self):
        self.color = WHITE
        self.body = [list(INITIAL_SNAKE_POSITION)]
        self.direction = INITIAL_DIRECTION

    @property
    def head(self):
        """Get the snake's head position."""
        return self.body[0]

    def change_direction(self, new_direction):
        """
        Change snake direction if valid (no 180-degree turns).

        Args:
            new_direction: One of 'UP', 'DOWN', 'LEFT', 'RIGHT'
        """
        opposites = {
            'UP': 'DOWN',
            'DOWN': 'UP',
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT'
        }

        if new_direction in opposites and opposites[new_direction] != self.direction:
            self.direction = new_direction

    def move(self):
        """
        Move the snake one step in current direction.

        Returns:
            The new head position.
        """
        new_head = self.head.copy()

        if self.direction == 'UP':
            new_head[1] -= GRID_SIZE
        elif self.direction == 'DOWN':
            new_head[1] += GRID_SIZE
        elif self.direction == 'LEFT':
            new_head[0] -= GRID_SIZE
        elif self.direction == 'RIGHT':
            new_head[0] += GRID_SIZE

        self.body.insert(0, new_head)
        return new_head

    def shrink(self):
        """Remove the tail segment (called when not eating food)."""
        if len(self.body) > 1:
            self.body.pop()
        else:
            self.body.pop()

    def check_wall_collision(self):
        """
        Check if snake head has hit a wall.

        Returns:
            True if collision detected, False otherwise.
        """
        head_x, head_y = self.head
        return (
            head_x < 0 or
            head_x >= SCREEN_WIDTH or
            head_y < 0 or
            head_y >= SCREEN_HEIGHT
        )

    def check_self_collision(self):
        """
        Check if snake head has hit its own body.

        Returns:
            True if collision detected, False otherwise.
        """
        for segment in self.body[1:]:
            if self.head[0] == segment[0] and self.head[1] == segment[1]:
                return True
        return False

    def reset(self):
        """Reset snake to initial state."""
        self.body = [list(INITIAL_SNAKE_POSITION)]
        self.direction = INITIAL_DIRECTION


class Food:
    """Represents the food item."""

    def __init__(self):
        self.color = RED
        self.position = self._generate_position()

    def _generate_position(self):
        """Generate a random position on the grid."""
        x = random.randrange(1, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE
        y = random.randrange(1, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE
        return [x, y]

    def respawn(self, snake_body=None):
        """
        Respawn food at a new random position.

        Args:
            snake_body: Optional list of snake body positions to avoid spawning on.
        """
        self.position = self._generate_position()

        # Ensure food doesn't spawn on the snake
        if snake_body:
            while self.position in snake_body:
                self.position = self._generate_position()

    def is_eaten(self, head_position):
        """
        Check if food has been eaten by the snake.

        Args:
            head_position: The snake's head position.

        Returns:
            True if food is at head position, False otherwise.
        """
        return (
            head_position[0] == self.position[0] and
            head_position[1] == self.position[1]
        )
