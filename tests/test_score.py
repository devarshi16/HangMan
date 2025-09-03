import os
import sys
from pathlib import Path

# Ensure project root is on the import path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from hangmanultimate.hangman import Game


def test_score_tracks_wins_and_losses(monkeypatch):
    # Prevent clear screen calls during tests
    monkeypatch.setattr(os, "system", lambda *args, **kwargs: None)

    Game.win = 0
    Game.lose = 0

    # Simulate a winning game
    game_win = Game(["dog"], "animals")
    game_win.success_stat = 1
    game_win.Score()

    assert Game.win == 1
    assert Game.lose == 0

    # Simulate a losing game
    game_lose = Game(["cat"], "animals")
    game_lose.success_stat = 0
    game_lose.Score()

    assert Game.win == 1
    assert Game.lose == 1
