import os
import shutil

class Zip:
    def __init__(self, source:str, destination:str):
        """
        zip a file or directory.

        Args:
        source: the source directory to zip
        destination: the destination to zip the file to

        'source' must be a directory
        'destination' can be a directory or a zip file
        """
        self.source     :str = self._set_source(source)
        self.destination:str = self._set_destination(destination)
        self.zip()

    def _set_source(self, source:str)->str:
        if os.path.exists(source):
            if os.path.isdir(source):
                return source
            raise FileNotFoundError('Source must be a directory')
        raise FileNotFoundError('Source does not exist')
    
    def _set_destination(self, destination:str)->str:
        if self._isdirlike(destination):
            self.format = 'zip'
            os.makedirs(destination,exist_ok=True)
            return os.path.join(destination,os.path.basename(self.source))
        
        elif destination.endswith((".zip", ".tar", ".gztar", ".bztar",".xztar")):
            if os.path.exists(destination):
                raise FileExistsError('Destination file already exists')
            self.format = destination.split('.')[-1]
            return destination.replace('.'+self.format,'')
        else:
            raise ValueError('if destination is not a directory, destination must be a zip filepath with extension .zip, .tar, .gztar, .bztar, or .xztar')
    
    def _isdirlike(self,path:str)->bool:
        '''
        if a path is dirlike or filelike
        '''
        return '.' not in path.split('\\')[-1]

    def zip(self)->None:
        shutil.make_archive(self.destination,self.format,self.source)

class Unzip:
    def __init__(self, source:str, destination:str):
        """
        unzip a zip file.

        Args:
        source: the source zip file to unzip
        destination: the destination to unzip the file to

        if source is a directory, then the first found zip file in the directory will be unzipped to the destination.
        """
        self.source     :str = self._set_source(source)
        self.destination:str = self._set_destination(destination)
        self.unzip()

    def _set_source(self, source:str)->str:
        if os.path.isdir(source):
            return self._get_zip_file(source)
        return source

    def _set_destination(self, destination:str)->str:
        if not os.path.exists(destination):
            os.makedirs(destination,exist_ok=True)
        return destination
    
    def _get_zip_file(self, source:str)->str:
        for file in os.listdir(source):
            if file.endswith((".zip", ".tar", ".gztar", ".bztar",".xztar")):
                return os.path.join(source,file)
        raise FileNotFoundError('No zip file found in the source directory')
    
    def unzip(self)->None:
        shutil.unpack_archive(self.source,self.destination)
