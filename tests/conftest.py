import os, sys

# Add the repository root to sys.path so tests can import simulate.py, detect.py, etc.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)