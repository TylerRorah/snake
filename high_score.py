"""High score persistence management."""

import os
import config


def load_high_score():
    """
    Load the high score from file.

    Returns:
        The high score as an integer, or 0 if file doesn't exist.
    """
    if os.path.exists(config.HIGH_SCORE_FILE):
        try:
            with open(config.HIGH_SCORE_FILE, 'r') as f:
                return int(f.read().strip())
        except (ValueError, IOError):
            return 0
    return 0


def save_high_score(score):
    """
    Save the high score to file.

    Args:
        score: The score to save.
    """
    try:
        with open(config.HIGH_SCORE_FILE, 'w') as f:
            f.write(str(score))
    except IOError:
        pass  # Silently fail if we can't write


def update_high_score(current_score, high_score):
    """
    Update high score if current score is higher.

    Args:
        current_score: The current game score.
        high_score: The existing high score.

    Returns:
        The new high score (may be same as old if not beaten).
    """
    if current_score > high_score:
        save_high_score(current_score)
        return current_score
    return high_score
