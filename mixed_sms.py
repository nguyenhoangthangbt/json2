import random,time
import pandas as pd

# t1 = ["Em rao tin BDS qua SMS tu dong!", "Em giup rao tin BDS qua SMS! ","Em chuyen gui SMS rao tin BDS! ","Em gui tin rao BDS qua SMS!"]
t2 = ["Em co dich vu gui tin nhan SMS rao tin BDS den 20.000 so dt Khach Hang Tiem Nang dang giao dich BDS tai HCM va lan can trong 3 thang gan nhat. ",
"Em co 20.000 so dt Khach Hang Tiem Nang dang giao dich BDS tai HCM va lan can trong 3 thang gan nhat. ",
"Duy nhat ben em co Danh sach 20.000 so dt Khach Hang Tiem Nang dang giao dich BDS tai HCM va lan can trong 3 thang gan nhat. ",
"Danh sach 20.000 so dt Khach Hang Tiem Nang dang giao dich BDS tai HCM va lan can trong 3 thang gan nhat, chi duy nhat ben em co! "]
t3 = ["Anh chi lien he em 0348009350 khi can gui SMS tu dong rao tin BDS nhe. ",
"Neu anh chi can gui tin nhan SMS rao tin BDS den danh sach nay hay lien he em nhe 0348009350. ",
"Anh chi LH em nhe 0348009350. Em se gui tin SMS tu dong den danh sach nay de rao tin BDS cho anh chi. ",
"So dt cua em 0348009350 anh chi lien he em khi can gui tin SMS tu dong den danh sach nay nhe. "]
t4 = ["Phi dich vu 100 vnd/tin a!",
"Gia re 100 d/tin a!",
"Chi co 100 dong/tin cho phi dich vu!",
"Phi dich vu 100d/tin a!"]

counter=1
sms_temp = []
for i4 in t4:
    for i3 in t3:
        for i2 in t2:           
                # print(f'*{counter}:', i1,i2,i3,i4,'\n')
                # time.sleep(1)
                sms1 = i2
                sms2 = i3+i4
                sms = {'sms1':sms1, 'sms2':sms2}
                sms_temp.append(sms)    
                # counter +=1
df =pd.DataFrame(sms_temp)
df.to_csv("sms_temp2.csv", sep=";")