import argparse
import os

from .mostRecent import MostRecent #type: ignore

def create_parser():
    parser = argparse.ArgumentParser(description='Quickly move most recent downloads to any working directory')
    parser.add_argument('-d','--destination',type=str,default = os.getcwd(),help='Destination folder to move the file to')
    parser.add_argument('-n','--num_files',type=int,default=1,help='Number of files to move')
    parser.add_argument('-m','--mkdir',type=bool,default=False,help='Create the destination directory if it doesn\'t exist')
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = dict(parser.parse_args()._get_kwargs())
    MostRecent(**args)
