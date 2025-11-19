"""Game state management."""


class GameState:
    """Manages the overall state of the game."""

    def __init__(self):
        self.score = 0
        self.running = True
        self.game_over = False
        self.paused = False

    def increment_score(self):
        """Increase score by 1."""
        self.score += 1

    def reset(self):
        """Reset game state to initial values."""
        self.score = 0
        self.running = True
        self.game_over = False
        self.paused = False

    def toggle_pause(self):
        """Toggle the paused state."""
        self.paused = not self.paused

    def end_game(self):
        """Mark the game as over."""
        self.game_over = True

    def stop_running(self):
        """Stop the game loop."""
        self.running = False
