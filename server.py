#!/usr/bin/env python3
"""
Readability MCP Server - Entry Point
This file maintains backward compatibility while using the new modular structure
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the server from the new location
from src.server import mcp

if __name__ == "__main__":
    mcp.run()