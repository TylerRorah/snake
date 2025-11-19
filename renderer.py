"""Renderer - handles all pygame drawing operations."""

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE,
    BLACK, WHITE, RED,
    SCORE_FONT, SCORE_FONT_SIZE,
    GAME_OVER_FONT, GAME_OVER_FONT_SIZE,
    FINAL_SCORE_FONT, FINAL_SCORE_FONT_SIZE
)


class Renderer:
    """Handles all pygame rendering operations."""

    def __init__(self, screen):
        self.screen = screen

    def clear(self):
        """Clear the screen with black background."""
        self.screen.fill(BLACK)

    def draw_snake(self, snake):
        """
        Draw the snake on screen.

        Args:
            snake: Snake entity to draw.
        """
        for segment in snake.body:
            pygame.draw.rect(
                self.screen,
                snake.color,
                pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE)
            )

    def draw_food(self, food):
        """
        Draw the food on screen.

        Args:
            food: Food entity to draw.
        """
        pygame.draw.rect(
            self.screen,
            food.color,
            pygame.Rect(food.position[0], food.position[1], GRID_SIZE, GRID_SIZE)
        )

    def draw_score(self, score):
        """
        Draw the current score at top of screen.

        Args:
            score: Current score value.
        """
        font = pygame.font.SysFont(SCORE_FONT, SCORE_FONT_SIZE)
        surface = font.render(f'Score : {score}', True, WHITE)
        rect = surface.get_rect()
        rect.midtop = (SCREEN_WIDTH / 2, 10)
        self.screen.blit(surface, rect)

    def draw_game_over(self, score):
        """
        Draw the game over screen.

        Args:
            score: Final score value.
        """
        self.clear()

        # Draw "YOU DIED" text
        font = pygame.font.SysFont(GAME_OVER_FONT, GAME_OVER_FONT_SIZE)
        surface = font.render('YOU DIED', True, RED)
        rect = surface.get_rect()
        rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.screen.blit(surface, rect)

        # Draw final score
        score_font = pygame.font.SysFont(FINAL_SCORE_FONT, FINAL_SCORE_FONT_SIZE)
        score_surface = score_font.render(f'Score : {score}', True, RED)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.25)
        self.screen.blit(score_surface, score_rect)

    def update_display(self):
        """Update the display to show all drawn elements."""
        pygame.display.flip()
