"""Tests for the GameState class."""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_state import GameState


class TestGameStateInitialization:
    """Tests for GameState initialization."""

    def test_initial_score_is_zero(self):
        state = GameState()
        assert state.score == 0

    def test_initial_running_is_true(self):
        state = GameState()
        assert state.running == True

    def test_initial_game_over_is_false(self):
        state = GameState()
        assert state.game_over == False

    def test_initial_paused_is_false(self):
        state = GameState()
        assert state.paused == False


class TestGameStateScore:
    """Tests for score management."""

    def test_increment_score(self):
        state = GameState()
        state.increment_score()
        assert state.score == 1

    def test_increment_score_multiple_times(self):
        state = GameState()
        for _ in range(5):
            state.increment_score()
        assert state.score == 5


class TestGameStateControl:
    """Tests for game state control."""

    def test_end_game(self):
        state = GameState()
        state.end_game()
        assert state.game_over == True

    def test_stop_running(self):
        state = GameState()
        state.stop_running()
        assert state.running == False

    def test_toggle_pause_from_unpaused(self):
        state = GameState()
        state.toggle_pause()
        assert state.paused == True

    def test_toggle_pause_from_paused(self):
        state = GameState()
        state.toggle_pause()
        state.toggle_pause()
        assert state.paused == False

    def test_toggle_pause_multiple_times(self):
        state = GameState()
        for _ in range(3):
            state.toggle_pause()
        assert state.paused == True


class TestGameStateReset:
    """Tests for game state reset."""

    def test_reset_clears_score(self):
        state = GameState()
        state.increment_score()
        state.increment_score()
        state.reset()
        assert state.score == 0

    def test_reset_clears_game_over(self):
        state = GameState()
        state.end_game()
        state.reset()
        assert state.game_over == False

    def test_reset_restores_running(self):
        state = GameState()
        state.stop_running()
        state.reset()
        assert state.running == True

    def test_reset_clears_paused(self):
        state = GameState()
        state.toggle_pause()
        state.reset()
        assert state.paused == False

    def test_full_reset(self):
        state = GameState()
        state.increment_score()
        state.end_game()
        state.stop_running()
        state.toggle_pause()
        state.reset()
        assert state.score == 0
        assert state.running == True
        assert state.game_over == False
        assert state.paused == False
