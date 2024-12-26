# What's new in 1.0.0 (26-12-2024)

- Improved `pydebugger` command
- `disasemble` command added
- Now the debugger will ignore pickletools errors
- Improved code readability
- Fixed all bugs in breakpoint handling (I think)
- Hooked `builtins.exit` so if the pickle bytecode calls it, python won't exit.
- This debugger now is using a patched version of pickletools to correctly disassemble the pickle bytecode without raising useless exceptions
