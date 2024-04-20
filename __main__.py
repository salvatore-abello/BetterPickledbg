import io
import sys
import secrets
import tempfile
import pickletools
from BetterPickledbg import _Unpickler
from BetterPickledbg.colors import *


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <picklefile>")
        sys.exit(1)

    try:
        pickle_file = open(sys.argv[1], "rb")
    except:
        print(redify("[!] Error: could not open pickle file"))
        sys.exit(1)

    try:
        tmpdir = tempfile.gettempdir()
        tmpname = tmpdir + '/tmp' + secrets.token_hex(6)
        with open(tmpname, "w") as tmpfile:
            pickletools.dis(pickle_file, out=tmpfile)
        pickle_disasm = open(tmpname, "r").read().split('\n')[:-2]
        __import__('os').remove(tmpname)
    except:
        print(redify("[!] Error: could not disassemble pickle file"))
        sys.exit(1)
    
    _Unpickler(io.BytesIO(open(sys.argv[1], "rb").read())).run()

if __name__ == "__main__":
    main()