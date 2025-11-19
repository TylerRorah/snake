"""Tests for the high score persistence module."""

import pytest
import sys
import os
import tempfile

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from high_score import load_high_score, save_high_score, update_high_score


class TestLoadHighScore:
    """Tests for loading high scores."""

    def test_load_returns_zero_when_file_missing(self, monkeypatch):
        # Use a non-existent file
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', 'nonexistent_file.txt')
        result = load_high_score()
        assert result == 0

    def test_load_returns_saved_score(self, tmp_path, monkeypatch):
        # Create a temporary file with a score
        score_file = tmp_path / "high_score.txt"
        score_file.write_text("42")
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        result = load_high_score()
        assert result == 42

    def test_load_returns_zero_for_invalid_content(self, tmp_path, monkeypatch):
        # Create a file with invalid content
        score_file = tmp_path / "high_score.txt"
        score_file.write_text("not a number")
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        result = load_high_score()
        assert result == 0

    def test_load_handles_empty_file(self, tmp_path, monkeypatch):
        # Create an empty file
        score_file = tmp_path / "high_score.txt"
        score_file.write_text("")
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        result = load_high_score()
        assert result == 0


class TestSaveHighScore:
    """Tests for saving high scores."""

    def test_save_creates_file(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        save_high_score(100)
        assert score_file.exists()
        assert score_file.read_text() == "100"

    def test_save_overwrites_existing_file(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        score_file.write_text("50")
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        save_high_score(75)
        assert score_file.read_text() == "75"


class TestUpdateHighScore:
    """Tests for updating high scores."""

    def test_update_returns_new_score_when_higher(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        result = update_high_score(100, 50)
        assert result == 100

    def test_update_saves_new_high_score(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        update_high_score(100, 50)
        assert score_file.read_text() == "100"

    def test_update_returns_old_score_when_lower(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        result = update_high_score(30, 50)
        assert result == 50

    def test_update_does_not_save_when_lower(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        score_file.write_text("50")
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        update_high_score(30, 50)
        assert score_file.read_text() == "50"

    def test_update_returns_same_when_equal(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        result = update_high_score(50, 50)
        assert result == 50

    def test_update_handles_zero_high_score(self, tmp_path, monkeypatch):
        score_file = tmp_path / "high_score.txt"
        monkeypatch.setattr(config, 'HIGH_SCORE_FILE', str(score_file))
        result = update_high_score(1, 0)
        assert result == 1
        assert score_file.read_text() == "1"
