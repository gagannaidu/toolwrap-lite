# toolwrap-lite

**toolwrap-lite** is a lightweight Python package that converts regular Python functions into OpenAI-compatible tool schemas using a simple decorator.

## Features
- No manual JSON writing
- Auto-extracts type hints and docstrings
- Export all tools into `tools.json`
- Plug into OpenAI, LangChain, or CrewAI easily

## Installation
```bash
pip install toolwrap-lite
```

## Usage
```python
from toolwrap_lite import tool, get_registered_tools

@tool
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

print(get_registered_tools())
```

## Export to JSON
```python
from toolwrap_lite import export_tools_to_json
export_tools_to_json("tools.json")
```

## Example Tool
```python
@tool
def summarize_tweets(username: str, count: int = 5, language: str = "en") -> str:
    """Summarize tweets from a username."""
    return "Summary..."
```
