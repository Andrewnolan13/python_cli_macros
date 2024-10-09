import argparse
import os

from .Zipper import Zip,Unzip


def create_parser():
    parser = argparse.ArgumentParser(description='Quickly move most recent downloads to any working directory')
    parser.add_argument('-m', '--mode', type=str, default = 'unzip', help='zip/unzip. Default is unzip')
    parser.add_argument('-s','--source', type=str, default = os.getcwd(), help='Source folder/(zipfile,folder) to zip/unzip the contents from. Default is current working directory')
    parser.add_argument('-d','--destination', type=str, default = os.getcwd(), help='Destination zipfile/folder to zip/unzip the contents to. Default is current working directory')
    return parser

def switch_mode(mode:str, **kwargs):
    if mode == 'zip':
        Zip(**kwargs)
    elif mode == 'unzip':
        Unzip(**kwargs)
    else:
        raise ValueError('Invalid mode. Please select either zip or unzip')
if __name__ == '__main__':
    parser = create_parser()
    kwargs = dict(parser.parse_args()._get_kwargs())
    switch_mode(**kwargs)
