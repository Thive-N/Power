import colorama
from typing import Any


def iprint(*args: Any, **kwargs: Any) -> None:
    """prints a informatory message
    """
    print(colorama.Fore.CYAN, "[i]", end='')
    print(colorama.Fore.RESET, end='')
    print(*args, **kwargs)


def wprint(*args: Any, **kwargs: Any) -> None:
    """prints a warning message
    """
    print(colorama.Fore.YELLOW, "[w]", end='')
    print(colorama.Fore.RESET, end='')
    print(*args, **kwargs)


def eprint(*args: Any, **kwargs: Any) -> None:
    """prints a error message
    """
    print(colorama.Fore.RED, "[e]", end='')
    print(colorama.Fore.RESET, end='')
    print(*args, **kwargs)
