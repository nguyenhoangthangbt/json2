import pandas as pd
import datetime,os,time

os.system("git add hcm_viettel.csv")
time.sleep(1)
os.system(
    f'git commit -m "changed at {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
time.sleep(1)
os.system('git push')
time.sleep(2)
os.system("git --version")
print('uploaded to github done!')
