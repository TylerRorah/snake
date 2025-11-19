"""Renderer - handles all pygame drawing operations."""

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE,
    BLACK, WHITE, RED, GREEN,
    SCORE_FONT, SCORE_FONT_SIZE,
    GAME_OVER_FONT, GAME_OVER_FONT_SIZE,
    FINAL_SCORE_FONT, FINAL_SCORE_FONT_SIZE,
    PAUSE_FONT, PAUSE_FONT_SIZE, INSTRUCTION_FONT_SIZE
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

    def draw_paused(self):
        """Draw the pause overlay."""
        # Semi-transparent overlay effect (darken the screen)
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        # Draw "PAUSED" text
        font = pygame.font.SysFont(PAUSE_FONT, PAUSE_FONT_SIZE)
        surface = font.render('PAUSED', True, WHITE)
        rect = surface.get_rect()
        rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.screen.blit(surface, rect)

        # Draw instruction
        inst_font = pygame.font.SysFont(PAUSE_FONT, INSTRUCTION_FONT_SIZE)
        inst_surface = inst_font.render('Press P to resume', True, WHITE)
        inst_rect = inst_surface.get_rect()
        inst_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
        self.screen.blit(inst_surface, inst_rect)

    def draw_game_over(self, score, high_score=None):
        """
        Draw the game over screen.

        Args:
            score: Final score value.
            high_score: Optional high score value.
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
        score_surface = score_font.render(f'Score: {score}', True, WHITE)
        score_rect = score_surface.get_rect()
        score_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.screen.blit(score_surface, score_rect)

        # Draw high score if provided
        if high_score is not None:
            if score >= high_score and score > 0:
                hs_text = f'NEW HIGH SCORE!'
                hs_color = GREEN
            else:
                hs_text = f'High Score: {high_score}'
                hs_color = WHITE
            hs_surface = score_font.render(hs_text, True, hs_color)
            hs_rect = hs_surface.get_rect()
            hs_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60)
            self.screen.blit(hs_surface, hs_rect)

        # Draw restart instruction
        inst_font = pygame.font.SysFont(SCORE_FONT, INSTRUCTION_FONT_SIZE)
        inst_surface = inst_font.render('Press R to restart or close window to quit', True, WHITE)
        inst_rect = inst_surface.get_rect()
        inst_rect.midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
        self.screen.blit(inst_surface, inst_rect)

    def update_display(self):
        """Update the display to show all drawn elements."""
        pygame.display.flip()
