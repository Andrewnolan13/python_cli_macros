# make 10 csvs with random data
# save them to ./data
# zip them to./zipped_data twice with different names as zip1.zip and zip2.zip

## Test 1 - passing a directory as source argument
# unzip them to ./unzipped_data

## Test 2 - passing a zip file as source argument
# unzip zip2.zip to ./unzipped_data

import os
import shutil
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..')) # add parent directory to sys.path

from zipit import Unzip

def make_csvs():
    os.makedirs('data/1',exist_ok=True)
    os.makedirs('data/2',exist_ok=True)
    for i in range(10):
        df = pd.DataFrame({'A':range(10),'B':range(10)})
        df.to_csv(f'data/1/data{i}.csv',index=False) if i % 2 == 0 else df.to_csv(f'data/2/data{i}.csv',index=False)

def zip_data():
    os.makedirs('zipped_data',exist_ok=True)
    shutil.make_archive('zip1','zip','data/1')
    shutil.make_archive('zip2','zip','data/2')

    shutil.move('zip1.zip','zipped_data')
    shutil.move('zip2.zip','zipped_data')

def test1():
    Unzip(source='zipped_data',destination='unzipped_data')

def test2():
    Unzip(source='zipped_data/zip2.zip',destination='unzipped_data/zip2_contents')

if __name__ == '__main__':

    for obj in os.listdir():
        if obj.endswith('.py'):
            continue
        if os.path.isdir(obj):
            shutil.rmtree(obj)
        else:
            os.remove(obj)


    make_csvs()
    zip_data()
    
    test1()
    test2()

    assert set(os.listdir('unzipped_data')) == {'data0.csv',  'data2.csv',  'data4.csv', 'data6.csv',  'data8.csv',  'zip2_contents'}
    assert set(os.listdir('unzipped_data/zip2_contents')) == {'data1.csv',  'data3.csv',  'data5.csv', 'data7.csv',  'data9.csv'}

    print('All tests passed')