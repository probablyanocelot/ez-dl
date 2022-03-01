# sheet-grab
GOAL:
routinely collect and sort spreadsheets(or other files) chronologically

CURRENTLY:
SheetHandler(name, url)

if file extension snippet from EXT is in url:     filename = name.extension
if not exists:                                    make directory  ./sheets/
if not exists:                                    make directory  ./sheets/[name]
if not exists file downloaded today:              download & save ./sheets/[name]/YYYY-MM-DD_[filename]
