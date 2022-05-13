import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from parent.subB.mod import fuga

if __name__ == '__main__':
    fuga()
