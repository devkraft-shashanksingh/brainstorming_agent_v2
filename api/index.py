import sys
import os

# Add the backend directory to the Python path so we can import from data_library
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from data_library.api import app

# This is required for Vercel to identify the entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
