import os
import shutil

DOWNLOADS = os.path.join(os.environ['HOMEDRIVE'],os.environ['HOMEPATH'],'Downloads')

def argMax(**kwargs):
    return max(kwargs, key=kwargs.get)

class MostRecent:
    """
    Simple class that looks at the most recent download in the user's download folder and moves it to the current working directory if destination isn't specified.
    """
    def __init__(self, destination:str=None, num_files:int=None, mkdir:bool=None):
        self.destination = destination or os.getcwd()
        self.num_files = num_files or 1
        self.mkdir = mkdir or False
        self.raiseErrors()
        self.move()

    def move(self,num_calls = 0)->None:
        src = self.getMostRecentFilepath()
        if self.mkdir and not os.path.exists(self.destination):
            os.makedirs(self.destination,exist_ok=True)
        shutil.move(src,self.destination)
        if num_calls + 1 < self.num_files:
            self.move(num_calls + 1) 
    
    def getMostRecentFilepath(self)->str:
        downloads_contents:map = map(lambda file:os.path.join(DOWNLOADS,file),os.listdir(DOWNLOADS))
        modified_times_table:dict = {file:os.path.getmtime(file) for file in downloads_contents}
        return argMax(**modified_times_table)
    
    def raiseErrors(self)->None:
        if not isinstance(self.num_files,int) or self.num_files < 1:
            raise ValueError('num_files must be an integer greater than 0')
        if not isinstance(self.mkdir,bool):
            raise ValueError('mkdir must be a boolean')
        elif not os.path.exists(self.destination) and not self.mkdir:
            raise FileNotFoundError('destination does not exist')


if __name__ == '__main__':
    print(os.environ)