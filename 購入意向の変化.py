
# coding: utf-8

# #### アサヒビールの購入意向の変化を表す変数作成したよ
# 全部の変数にはまだ応用できてない！

# In[ ]:

import pandas as pd


# In[ ]:

df = pd.read_csv("/Volumes/Sony_8GT/NRI_データ解析コンペ/アンケートデータ/CSV/メインデータ_2017.csv")


# In[ ]:

df.head()


# In[ ]:

#欠損値処理
df = df[df["PI_01_752601"]!=' ']
df = df[df["PI_02_752601"]!=' ']
len(df)


# In[ ]:

#object型→int型
int1_list = list(df["PI_01_752601"].values.flatten())
int1_list = [int(x) for x in int1_list]

int2_list = list(df["PI_02_752601"].values.flatten())
int2_list = [int(x) for x in int2_list]

df["PI_01_752601"] = int1_list
df["PI_02_752601"] = int2_list


# |  |1.ぜひ買いたい| 2.買いたい | 3.わからない |4.買いたくない|
# |:-----:|:----:|:-----:|:-----:|:----:|
# | **1.ぜひ買いたい** | 0| -1 |-2|-3|
# | **2.買いたい** | 1| 0 |-1|-2|
# | **3.わからない** | 2| 1 |0|-1|
# | **4.買いたくない** | 3| 2 |1|0|
# 

# In[ ]:

#態度変化
df["trans_752601"] = df["PI_01_752601"]-df["PI_02_752601"] 


# In[ ]:

df.groupby("trans_752601").size()


# 基本的には意向は変化してないけどポジティブ（ネガティブ）な変化も一定数いるね.

# In[ ]:



