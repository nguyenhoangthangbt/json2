import pandas as pd
import json,datetime,os,time,sqlalchemy,sqlite3

conn = sqlite3.connect(
    r'D:\OneDrive - 5TB\Home-PC-working\10 Programming\python\2batdongsan\contact_BDS.db')
df = pd.read_sql("select * from alo_all_brokers", con=conn)
# df = pd.read_csv(r"D:\OneDrive - 5TB\Home-PC-working\10 Programming\python\messages\json2\contacts_sample.csv", converters={
#                 i: str for i in range(100)})
df['updated_at'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
df.to_csv(
    r"D:\OneDrive - 5TB\Home-PC-working\10 Programming\python\0messages\json2\contacts_alo_all_brokers.csv")
os.system("git add contacts_alo_all_brokers.csv")
time.sleep(1)
os.system(
    f'git commit -m "changed at {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
time.sleep(1)
os.system('git push')
time.sleep(2)
os.system("git --version")
print('uploaded to github done!')
