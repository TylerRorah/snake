"""Snake Game - Main entry point."""

import sys
import time
import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GAME_OVER_DELAY
from game_engine import GameEngine
from renderer import Renderer


def main():
    """Main game loop."""
    # Initialize pygame
    pygame.init()

    # Create screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    # Initialize game components
    engine = GameEngine()
    renderer = Renderer(screen)

    # Main game loop
    while engine.is_running():
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.stop()
            elif event.type == pygame.KEYDOWN:
                engine.handle_input(event.key)

        # Update game state
        if not engine.is_game_over():
            game_continues = engine.update()

            if not game_continues:
                # Game over - show death screen
                renderer.draw_game_over(engine.get_score())
                renderer.update_display()
                time.sleep(GAME_OVER_DELAY)
                engine.stop()
                continue

        # Render
        renderer.clear()
        renderer.draw_snake(engine.snake)
        renderer.draw_score(engine.get_score())
        renderer.draw_food(engine.food)
        renderer.update_display()

        # Cap frame rate
        clock.tick(FPS)

    # Cleanup
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
