import os

class PrintTree:
    def __init__(self,root:str=None,ignore:str=None):
        self.root = root or os.getcwd()
        self.ignore = tuple(ignore.split(',')) or tuple()
        self.printTree()
    def printTree(self):
        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in self.ignore]
            level = root.replace(self.root, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))
if __name__ == '__main__':
    PrintTree(ignore = '.git,bin,lib')