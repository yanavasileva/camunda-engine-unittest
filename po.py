import os
import datetime

now = datetime.datetime.now()
now = str(now.strftime("%Y-%m-%d %H:%M"))
os.chdir(".")
os.system("git add .")
os.system("git commit -m 'TODO'")

import os

os.chdir("C:/workspace/camunda-engine-unittest")
os.system("git add .")
os.system("git commit -m 'TODO'")
