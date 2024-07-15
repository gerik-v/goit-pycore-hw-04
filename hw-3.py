import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(path, indent=""):
    try:
        directory = Path(path)
        if not directory.is_dir():
            print(f"{Fore.RED}Error: {path} is not a directory")
            return
        
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                print_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory_path>")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)
