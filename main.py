"""Snake Game - Main entry point."""

import sys
import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game_engine import GameEngine
from renderer import Renderer
from high_score import load_high_score, update_high_score


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

    # Load high score
    high_score = load_high_score()

    # Main game loop
    while engine.is_running():
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.stop()
            elif event.type == pygame.KEYDOWN:
                engine.handle_input(event.key)

        # Update game state (only if not paused and not game over)
        if not engine.is_game_over() and not engine.is_paused():
            game_continues = engine.update()

            if not game_continues:
                # Game over - update high score
                high_score = update_high_score(engine.get_score(), high_score)

        # Render
        if engine.is_game_over():
            # Show game over screen
            renderer.draw_game_over(engine.get_score(), high_score)
        else:
            # Normal gameplay rendering
            renderer.clear()
            renderer.draw_snake(engine.snake)
            renderer.draw_score(engine.get_score())
            renderer.draw_food(engine.food)

            # Show pause overlay if paused
            if engine.is_paused():
                renderer.draw_paused()

        renderer.update_display()

        # Cap frame rate
        clock.tick(FPS)

    # Cleanup
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
