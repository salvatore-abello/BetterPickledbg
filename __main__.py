import io
import sys
import secrets
import tempfile
import pickletools
from BetterPickledbg import _Unpickler
from BetterPickledbg.colors import *


def main():
    _Unpickler(sys.argv[1] if len(sys.argv) >= 2 else None).run()

if __name__ == "__main__":
    main()