# ez-dl
GOAL:<br>
download and sort files chronologically

CURRENTLY:<br><br>
Downloader(name, url)

1.  if file extension snippet from EXT is in url:     
    * filename = name.extension<br>
2.  if not exists ./data/:
    * make directory  ./data/<br>
3.  if not exists ./data/[name]:
    * make directory  ./data/[name]<br>
4.  if not exists file downloaded today:
    * download & save ./data/[name]/YYYY-MM-DD_[filename]<br>
