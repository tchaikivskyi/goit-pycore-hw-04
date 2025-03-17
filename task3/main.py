import sys
from pathlib import Path
from colorama import init, Fore

def print_directory_structure(directory, prefix=""):
    try:
        entries = sorted(Path(directory).iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
        for index, entry in enumerate(entries):
            connector = "┗━ " if index == len(entries) - 1 else "┣━ "
            if entry.is_dir():
                print(Fore.BLUE + prefix + connector + "DIR -> " + entry.name + Fore.RESET)
                print_directory_structure(entry, prefix + ("   " if index == len(entries) - 1 else "┃  "))
            else:
                print(Fore.GREEN + prefix + connector + "FILE -> " + entry.name + Fore.RESET)
    except PermissionError:
        print(Fore.RED + prefix + "[ACCESS DENIED]" + Fore.RESET)

def main():
    init()
    if len(sys.argv) != 2:
        print(Fore.RED + "Please provide a directory path." + Fore.RESET)
        print("Usage example: python hw03.py /path/to/directory")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + "Directory or file not exist." + Fore.RESET)
        sys.exit(1)
    
    print(Fore.YELLOW + f"[ROOT] {directory} " + Fore.RESET)
    print_directory_structure(directory)

if __name__ == "__main__":
    main()
