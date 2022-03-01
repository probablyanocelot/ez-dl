import urllib.request
import os
from os.path import exists

EXT = ['.csv', '.xlsx', '.json']
DEST = './sheets/'

URLS = {
    "Take5": "https://data.ny.gov/api/views/dg63-4siq/rows.csv?accessType=DOWNLOAD&sorting=true",
    "Cash4Life": "https://data.ny.gov/api/views/kwxv-fwze/rows.csv?accessType=DOWNLOAD&sorting=true",
    "Win4": "https://data.ny.gov/api/views/hsys-3def/rows.csv?accessType=DOWNLOAD&sorting=true",
    "PowerBall": "https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD&sorting=true",
    "LotteryNy": "https://data.ny.gov/api/views/6nbc-h7bj/rows.csv?accessType=DOWNLOAD&sorting=true",
    "MegaMillions": "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD&sorting=true",
    "QuickDraw": "https://data.ny.gov/api/views/7sqk-ycpk/rows.csv?accessType=DOWNLOAD&sorting=true",
    "Pick10": "https://data.ny.gov/api/views/bycu-cw7c/rows.csv?accessType=DOWNLOAD&sorting=true",
    "SweetMillion": "https://data.ny.gov/api/views/xjtd-9p3n/rows.csv?accessType=DOWNLOAD&sorting=true",
}


class SheetHandler(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.filename = self.get_filename()
        self.sheetdir = self.create_sheetdir()
        self.download()

    def get_filename(self):
        """
        self.name + appropriate extension
        """
        for xtn in EXT:
            if xtn in URLS[self.name]:
                filename = self.name + xtn
                return filename

    def create_sheetdir(self):
        """
        Create /sheets & /sheets/self.name/ if not exists
        """
        if not os.path.exists(DEST):
            os.mkdir(DEST)
        if not os.path.exists(DEST + self.name):
            os.mkdir(DEST + self.name + '/')
        sheetdir = DEST + self.name + '/'
        return sheetdir

    def download(self):
        print(f'Beginning download...       {self.name}')
        urllib.request.urlretrieve(
            self.url, filename=self.sheetdir + self.filename)
        print('Download complete.')


if __name__ == '__main__':
    for name in URLS:
        url = URLS[name]
        SheetHandler(name, url)
    print('All sheets downloaded.')
