
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Detect environment
IS_VERCEL = os.getenv("VERCEL") == "1"

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model Configuration
GEMINI_THINKING_MODEL = "gemini-3-flash-preview"
GEMINI_RAG_MODEL = "gemini-3-flash-preview"

# Constants
FILE_SEARCH_STORE_NAME = "pharma-brand-library"

if IS_VERCEL:
    # Vercel has a read-only filesystem except for /tmp
    BASE_DATA_DIR = Path("/tmp/data")
else:
    BASE_DATA_DIR = Path("./data")

DB_PATH = BASE_DATA_DIR / "agents.db"
SESSIONS_DB_PATH = BASE_DATA_DIR / "sessions.db"
DOCS_PATH = BASE_DATA_DIR / "documents"

# Ensure directories exist (only if writable)
try:
    BASE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_PATH.mkdir(parents=True, exist_ok=True)
except Exception as e:
    print(f"Warning: Could not create directories: {e}")

# Validate API Key but don't crash immediately at module load
# This allows health checks or other endpoints to run if the key is provided late
def validate_config():
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
