#!/usr/bin/env python3
"""
Simple startup script for the Text to PowerPoint Generator
"""

import uvicorn
import os
from pathlib import Path

def main():
    """Start the FastAPI application"""
    
    # Create temp directory if it doesn't exist
    temp_dir = Path("temp_files")
    temp_dir.mkdir(exist_ok=True)
    
    # Check if requirements are installed
    try:
        import fastapi
        import openai
        from pptx import Presentation
        print("✅ All dependencies are installed")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return
    
    # Start the server
    print("🚀 Starting Text to PowerPoint Generator...")
    print("📱 Open your browser to: http://localhost:8000")
    print("📁 Frontend: http://localhost:8000/index.html")
    print("🔧 API docs: http://localhost:8000/docs")
    print("⏹️  Press Ctrl+C to stop")
    print("-" * 50)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
