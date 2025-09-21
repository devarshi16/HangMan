# Contributing

Thank you for considering contributing to HangMan!

## Setting up the project

1. Fork the repository and clone your fork.
2. Create a virtual environment and activate it.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. *(Optional)* Install the project in editable mode:
   ```
   pip install -e .
   ```
5. Run a quick syntax check:
   ```
   python -m compileall src/hangmanultimate
   ```
6. Execute the test suite:
   ```
   python -m pytest
   ```

## Pull requests

- Use a feature branch for your work.
- Ensure the syntax check passes before submitting.
- Update documentation and add tests when applicable.
- Describe your changes in the pull request.
