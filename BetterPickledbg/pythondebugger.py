from .colors import *
import builtins


class PythonDebugger:
    def __init__(self, other):
        self.other = other
    
    def run(self):
        while True:
            try:
                code = input(greenify("pyd @ "))
                match code:
                    case "exit" | "quit" | "q":
                        raise KeyboardInterrupt
                    case _:
                        try:
                            result = eval(code, __builtins__, self.other)
                        except SyntaxError:
                            result = exec(code, __builtins__, self.other)

                match type(result):
                    case builtins.dict:
                        print(colorize_dict(result))
                    case builtins.int | builtins.float:
                        print(result)
                    case builtins.list | builtins.tuple:
                        print(colorize_array(result))
                
            except Exception as e:
                print(redify(f"{e.__class__.__name__}: {e}"))

            except KeyboardInterrupt:
                print(redify("\n[+] Exiting..."))
                break