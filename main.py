import urllib.request
import os
from os.path import exists
from datetime import date


URLS = {
    "Take5": "https://data.ny.gov/api/views/dg63-4siq/rows.csv?accessType=DOWNLOAD&sorting=true",
    "Cash4Life": "https://data.ny.gov/api/views/kwxv-fwze/rows.csv?accessType=DOWNLOAD&sorting=true",
    "Win4": "https://data.ny.gov/api/views/hsys-3def/rows.csv?accessType=DOWNLOAD&sorting=true",
    "PowerBall": "https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD&sorting=true",
    "LotteryNy": "https://data.ny.gov/api/views/6nbc-h7bj/rows.csv?accessType=DOWNLOAD&sorting=true",
    "MegaMillions": "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD&sorting=true",
    "Pick10": "https://data.ny.gov/api/views/bycu-cw7c/rows.csv?accessType=DOWNLOAD&sorting=true",
    "SweetMillion": "https://data.ny.gov/api/views/xjtd-9p3n/rows.csv?accessType=DOWNLOAD&sorting=true",
    "QuickDraw": "https://data.ny.gov/api/views/7sqk-ycpk/rows.csv?accessType=DOWNLOAD&sorting=true",
}


class KeyValPair(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class TargetFile(KeyValPair):
    EXT = ['.csv', '.xlsx', '.json']
    DEST = './data/'

    """
        TargetFile('desired filename', 'download url'),
            - makes directories for file 
    """

    def __init__(self, name, url):
        super().__init__(name, url)
        self.name = name
        self.url = url
        self.filename = self.get_filename()
        self.filedir = self.make_dirs()

    def get_filename(self):
        """
                # NEED TO USE ALT METHOD OF FINDING FILETYPE

        self.name + appropriate extension
        """
        for xtn in self.__class__.EXT:
            # more modular approach may be needed
            if xtn in self.url:
                filename = self.name + xtn
                return filename
            else:
                print("NEED TO USE ALT METHOD OF FINDING FILETYPE")

    def make_dirs(self):
        """
        Create /sheets & /sheets/self.name/ if not exists
        """
        filedir = self.__class__.DEST + self.name + '/'

        if not os.path.exists(self.__class__.DEST):
            os.mkdir(self.__class__.DEST)
        if not os.path.exists(filedir):
            os.mkdir(filedir)
        return filedir


# Split into two classes;
# Downloader & (Scheduler?)
class Downloader(TargetFile):
    def __init__(self, name, url):
        super().__init__(name, url)
        self.download()

    def download(self):
        '''
        If there is a file for today, don't download it

            today_file_dir = sheets/self.name/str(today) +_+ self.filename
        '''

        today = date.today()
        today_file_dir = self.filedir + str(today) + '_' + self.filename

        if os.path.isfile(today_file_dir):
            print(f'ALREADY EXISTS :            {str(today)}_{self.filename}')

        else:
            print(f'Beginning download...       {self.name}')
            urllib.request.urlretrieve(self.url, filename=today_file_dir)
            print('Download complete.')


class BatchDownload(Downloader):
    def __init__(self, dataset):
        # super().__init__(key, value)
        self.dataset = dataset
        self.download()

    def download(self):
        for name in self.dataset:
            url = self.dataset[name]
            Downloader(name, url)
        print('All sheets downloaded.')


if __name__ == '__main__':
    batch_download = BatchDownload(URLS)
    # for name in URLS:
    #     url = URLS[name]
    #     Downloader(name, url)
