from .colors import *
import builtins


class PythonDebugger:
    def __init__(self, context):
        self.context = context
        self.builtins = __builtins__.copy()
        self.builtins.update({"dump": self.__dump})  
    
    def __dump(self):
        for key, value in self.context.items():
            print(f"{key} = {value}")
        return 

    def run(self):
        while True:
            try:
                code = input(greenify("pyd >>> "))
                match code:
                    case "exit" | "quit" | "q":
                        raise KeyboardInterrupt
                    case "dump":
                        self.__dump()
                        continue
                    case _:
                        try:
                            result = eval(code, self.builtins, self.context)
                        except SyntaxError:
                            result = exec(code, self.builtins, self.context)

                match type(result):
                    case builtins.dict:
                        print(colorize_dict(result))
                    case builtins.int | builtins.float:
                        print(result)
                    case builtins.list | builtins.tuple:
                        print(colorize_array(result))
                    case _:
                        print(result)
                
            except Exception as e:
                print(redify(f"{e.__class__.__name__}: {e}"))

            except KeyboardInterrupt:
                print(redify("\n[+] Exiting..."))
                break
