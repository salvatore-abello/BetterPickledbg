import sys
import readline
from BetterPickledbg import _Unpickler


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
        
    _Unpickler(sys.argv[1]).run()

if __name__ == "__main__":
    main()
