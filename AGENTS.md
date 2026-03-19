# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

AI_NovelGenerator is a Python desktop GUI application (CustomTkinter) that uses LLMs to generate long-form novels chapter-by-chapter. See `README.md` for full feature list and usage instructions.

### Running the application

- Entry point: `python main.py`
- This is a GUI app requiring a display. In Cloud Agent VMs, start Xvfb first:
  ```
  Xvfb :99 -screen 0 1280x1024x24 -ac &
  export DISPLAY=:99
  python main.py
  ```
- The app requires `python3-tk` system package (not included in pip dependencies).

### Linting and testing

- No linting tools (flake8, pylint, ruff, etc.) or test frameworks (pytest, unittest) are configured in this project.
- No automated tests exist. Manual GUI testing via `computerUse` subagent is the primary verification method.
- To verify imports work: `python -c "import customtkinter; import langchain; import chromadb; import openai; print('OK')"`

### Key dependencies

- All Python dependencies are pinned in `requirements.txt` (install via `pip install -r requirements.txt`).
- Heavy ML packages (PyTorch, Transformers, sentence-transformers) make initial install slow (~2 min).
- ChromaDB runs embedded in-process — no separate database server required.

### Configuration

- Copy `config.example.json` to `config.json` and fill in API keys to use LLM features.
- The GUI works without API keys configured, but generation features require at least one valid LLM API key.

### Gotchas

- `pyreadline3` in `requirements.txt` is Windows-only but installs harmlessly on Linux.
- The `pyproject.toml` and `.python-version` files are gitignored — the project uses plain pip, not uv/poetry.
