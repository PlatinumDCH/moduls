from pathlib import Path
from colorama import Fore, init
import sys
from typing import Protocol

class IFileNameCplorizer(Protocol):
    """interface for set color"""

    def get_color(self, file:Path) -> str: ...

class FileNameColorizer(IFileNameCplorizer):
    def get_color(self, file:Path):
        if file.is_dir():
            return Fore.BLUE
        elif file.suffix == '.py':
            return Fore.YELLOW
        elif file.suffix == '.ipynb':
            return Fore.MAGENTA
        elif file.suffix in ['.txt', ".md"]:
            return Fore.GREEN
        else:
            return Fore.GREEN

class IDirectoryPrinter(Protocol):
    def print(self, path:Path, ident:str='')->None: ...

class DirectoryPrinter(IDirectoryPrinter):
    """exemple description"""
    def __init__(self, colorizer: IFileNameCplorizer):
        self.colorizer = colorizer
    
    def print(self, path:Path, ident:str = "") -> None:
        if path.is_dir():
            print(f'{ident}{Fore.BLUE}{path.name}')
            for item in path.iterdir():
                self.print(item, ident +'    ')
        else:
            color = self.colorizer.get_color(path)
            print(f'{ident}{color}{path.name}')

class DirectoryExplorer:
    """facade for job with directory"""
    def __init__(self, printer: IDirectoryPrinter):
        self.printer = printer
    
    def explore(self, path:Path)->None:
        if path.is_dir() and path.exists():
            self.printer.print(path)
        else:
            print(Fore.RED + 'Path not found or path is not a directory')

if __name__ == "__main__":

    import sys

    init(autoreset=True)

    if len(sys.argv) != 2:
        print(Fore.RED + "Not found path argument.")
        sys.exit(1)

    path = Path(sys.argv[1])

    colorizer = FileNameColorizer()
    printer = DirectoryPrinter(colorizer)
    explorer = DirectoryExplorer(printer)

    explorer.explore(path)
