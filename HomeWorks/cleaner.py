import os
import datetime
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join("./", f))]

for homeworkFile in onlyfiles:
    now = datetime.datetime.now()
    fileTime = os.path.getmtime(homeworkFile)
    if ((time.time() - file_time) / 3600 > 24*7):
        if homeworkFile != 'cron.py' or homeworkFile != 'cleaner.py':
            os.remove(homeworkFile)