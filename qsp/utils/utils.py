from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

from rich import print as print_color


def find_all_strings(nested_list) -> list:
    strings = []
    if isinstance(nested_list, str):
        return [nested_list]
    for item in nested_list:
        if isinstance(item, list):
            strings.extend(find_all_strings(item))
        elif isinstance(item, str):
            strings.append(item)
    return strings


class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
                A loader-like context manager

                Args:
                    desc (str, optional): The loader's description. Defaults to "Loading...".
                    end (str, optional): Final print. Defaults to "Done!".
                    timeout (float, optional): Sleep time between prints. Defaults to 0.1.

                from:
        https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
        """

        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="\r", flush=True)
        print_color(f"{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


def get_dynamic_function_string(function_name: str, function_parameters: str):
    return f"@instance.command()\n@framework_command(validator, workflow=workflow, defaults=dynamic_function_defaults,name=function_name,)\ndef {function_name}({function_parameters}): pass"  # noqa
