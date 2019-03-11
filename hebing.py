import pandas as pd

import os

SaveFile_Name = r'lianjia_all.csv'


file_list = os.listdir('D:\statistics\iris\lianjia\data')

df = pd.read_csv(file_list[0])


df.to_csv(SaveFile_Name, encoding="utf_8_sig", index=False)


for i in range(1, len(file_list)):
    df = pd.read_csv(file_list[i])

    df.to_csv(SaveFile_Name, encoding="utf_8_sig", index=False, header=False, mode='a+')