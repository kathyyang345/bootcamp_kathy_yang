"""
Small config helper: centralizes .env loading and key access
so notebooks and scripts don't repeat this logic.
"""

from pathlib import Path
import os
from dotenv import load_dotenv # type: ignore


def load_env():
    """Load environment variables from a .env file in this folder."""
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)


def get_key(name, default=None):
    """Read a single environment variable, with an optional default."""
    return os.getenv(name, default)


# Centralized paths, built from environment or sensible defaults
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(get_key("DATA_DIR", str(PROJECT_ROOT / "data")))