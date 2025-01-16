import os
import time
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter
from tkinter import filedialog



class DirectoryTree:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def generate_tree(self):
        tree_structure = self._generate_tree(self.root_dir)
        return tree_structure

    def _generate_tree(self, current_dir, prefix=""):
        tree = []
        contents = os.listdir(current_dir)
        contents.sort()
        for i, name in enumerate(contents):
            path = os.path.join(current_dir, name)
            connector = "└── " if i == len(contents) - 1 else "├── "
            tree.append(f"{prefix}{connector}{name}")
            if os.path.isdir(path):
                extension = "    " if i == len(contents) - 1 else "│   "
                tree.extend(self._generate_tree(path, prefix + extension))
        return tree

    def display_tree(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.root_dir}/")
        tree_structure = self.generate_tree()
        for line in tree_structure:
            print(line)

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, tree):
        self.tree = tree

    def on_any_event(self, event):
        self.tree.display_tree()

def create_parser():
    parser = argparse.ArgumentParser(description='watch changes to a directory tree in real time')
    parser.add_argument('-c', '--choose', type=bool, default = False, help='Choose a directory to watch')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.choose == True:
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        folder_path = filedialog.askdirectory()
    else:
        folder_path = os.getcwd()
    if folder_path == "":
        print("No directory selected. Exiting...")
        exit()

    os.chdir(folder_path)
    path = "."  # Replace with the directory you want to monitor
    tree = DirectoryTree(path)
    event_handler = ChangeHandler(tree)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping the observer")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()