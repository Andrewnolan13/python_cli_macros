# make 10 csvs with random data
# save them to ./data
# zip them to./zipped_data twice with different names as zip1.zip and zip2.zip
# zip to current working directory

import os
import shutil
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..')) # add parent directory to sys.path

from zipit import Zip

def make_csvs():
    os.makedirs('data/1',exist_ok=True)
    os.makedirs('data/2',exist_ok=True)
    for i in range(10):
        df = pd.DataFrame({'A':range(10),'B':range(10)})
        df.to_csv(f'data/1/data{i}.csv',index=False) if i % 2 == 0 else df.to_csv(f'data/2/data{i}.csv',index=False)
    
def zip_data():
    Zip(source='data/1',destination='zipped_data/zip1.zip')
    Zip(source='data/2',destination='zipped_data/zip2.zip')
    Zip(source='data/1',destination=os.getcwd())

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

    assert set([f for f in os.listdir() if not f.endswith('.py')]) == {'data', 'zipped_data', 'zipped_data', '1.zip'}
    assert set(os.listdir('zipped_data')) == {'zip1.zip', 'zip2.zip'}

    print('All tests passed')