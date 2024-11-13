import argparse
import os

from .printTree import PrintTree #type: ignore

def create_parser():
    parser = argparse.ArgumentParser(description='show the directory tree')
    parser.add_argument('-r','--root',type=str,default = os.getcwd(),help='root folder to start the tree')
    parser.add_argument('-i','--ignore',type=str,default='',help='comma separated list of folders to ignore')
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = dict(parser.parse_args()._get_kwargs())
    PrintTree(**args)