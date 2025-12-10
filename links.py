import pandas as pd
import xlwings as xw
import datetime as dt
import argparse
import os


warning = '''
Your links need to be from columns A to C
Starting with Old link, then an indicator column, called replace and finally new link.
Update times will be printed in to column D. 
'''

__all__ = ['linksToClip','UpdateLinks']

def linksToClip():
    wb = xw.books.active
    ws = wb.sheets.active
    links = wb.api.LinkSources()
    df = pd.DataFrame(data = links, columns = ['Old Link'])
    df.to_clipboard(index = False)
    print("links copied to clipboard")

class UpdateLinks:
    def __init__(self):
        print(warning)
        self.wb = xw.books.active
        self.ws = self.wb.sheets.active
        self.rng = self.ws.range('A2:C100')
    
    @property
    def links(self):
        return pd.DataFrame(data = self.rng.value, columns = 'Old Replace New'.split()).dropna(how = 'all')

    def update_links(self):
        print(self.links)
        if not self.links.New.apply(os.path.exists).all():
            msg = self.links.loc[~self.links.New.apply(os.path.exists),'New'].values.tolist()
            raise ValueError('Not all new links exist. Please check the paths.\nNon-existent links:\n{}'.format('\n'.join(msg)))

        for idx,row in self.links.iterrows():
            if bool(row['Replace']):
                
                old = row['Old']
                new = row['New']
                
                print('updating\nFrom :"{}"\nTo :"{}"\n\n\n'.format(old,new))
                ref = 'D{}'.format(idx+2)

                self.wb.api.ChangeLink(old,new)
                rng = self.ws.range(ref)
                rng.value = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def parse_args():
    '''decide between copying to clipboard or updating. default is to update'''
    args = argparse.ArgumentParser(description='Update links in the active workbook.')
    args.add_argument('-m','--mode', choices=['update','copy'], default='update', help='Mode of operation: update or copy links to clipboard.')
    return args.parse_args()
    


if __name__ == '__main__':
    args = parse_args()
    if args.mode == 'update':
        updater = UpdateLinks()
        updater.update_links()
    elif args.mode == 'copy':
        linksToClip()
    else:
        raise ValueError('Invalid mode. Use "update" or "copy".')
