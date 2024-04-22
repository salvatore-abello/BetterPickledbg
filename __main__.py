import sys
from BetterPickledbg import _Unpickler


def main():
    _Unpickler(sys.argv[1] if len(sys.argv) >= 2 else None).run()

if __name__ == "__main__":
    main()