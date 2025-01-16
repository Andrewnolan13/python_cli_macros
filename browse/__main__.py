import argparse
from .edge import Edge

def create_parser():
    parser = argparse.ArgumentParser(description='open an instance of ms edge')
    parser.add_argument('-u','--url',type=str,default = 'google',help='type a url to go to or use a predefined one. default is google.')
    parser.add_argument('-s','--saveUrlName',type=str,default = '',help='save the entered url with a name for later use.')
    parser.add_argument('-a','--alias',type=bool,default = False,help='show all aliases and their urls.')

    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = dict(parser.parse_args()._get_kwargs())
    Edge(**args)