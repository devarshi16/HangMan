"""Basic tests for the HangMan package."""

from pathlib import Path
import importlib
import sys


# Allow importing without installing the package
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))


def test_import():
    """Ensure the package can be imported."""
    importlib.import_module("hangmanultimate")
