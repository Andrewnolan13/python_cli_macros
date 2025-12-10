import xlwings as xw
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(description='Save all open workbooks. Optionally, close them.')
    parser.add_argument('-c', '--close', default=False, action='store_true',
                        help='Close the workbooks after saving.')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()

    for book in xw.books:
        print('Saving {}'.format(book.name))
        book.save()

    if args.close:
        print("Closing all open workbooks...")
        os.system('taskkill /f /im excel.exe')