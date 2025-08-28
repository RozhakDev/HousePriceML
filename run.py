import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from src.app import run_app

if __name__ == '__main__':
    run_app(debug=True)