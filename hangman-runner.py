"""Run the hangman game without installing the package."""

from pathlib import Path
import sys

# Allow running from the project root when using the src layout
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from hangmanultimate.hangman import main


if __name__ == "__main__":
    main()
