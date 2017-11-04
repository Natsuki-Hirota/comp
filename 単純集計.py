
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

main = pd.read_csv("/Volumes/Sony_8GT/H29/NRI_データ解析コンペ/アンケートデータ/CSV/メインデータ_2017.csv",encoding="shift-jis")


# In[3]:

fre1 = pd.read_table("/Volumes/Sony_8GT/H29/NRI_データ解析コンペ/Web/Webアクセス頻度（20170128-20170228）.txt")
fre2 = pd.read_table("/Volumes/Sony_8GT/H29/NRI_データ解析コンペ/Web/Webアクセス頻度（20170301-20170401）.txt")


# In[9]:

book1 = pd.read_csv("ブック1.csv",encoding="shift-jis",header=None)


# In[5]:

main.head()


# In[6]:

fre1.head()


# In[10]:

book1.head()


# In[11]:

access_to_buy = book1.dropna(subset=[1])
access_to_buy[1].unique()


# In[103]:

#アクセス頻度のリスト
access_array = access_to_buy[1]
access_list = access_array.tolist()
access_list


# In[13]:

#購買リスト
#アクセス頻度のリスト
buy_array = access_to_buy[0]
buy_list = buy_array.tolist()
buy_list


# In[14]:

#購買リスト
#アクセス頻度のリスト
item_array = access_to_buy[2]
item_list = item_array.tolist()
item_list


# In[15]:

#集計df
matome = pd.DataFrame(None)
matome["メインデータ変数名"] = buy_list
matome["アクセス頻度変数名"] = access_list
matome["商品名"] = item_list
matome.head()


# In[17]:

matome["購入実態2月"] = 0
matome["購入実態3月"] = 0
matome.head()


# In[18]:

matome["購入実態2月"][matome["商品名"].str.contains("02/")] = 1
matome["購入実態3月"][matome["商品名"].str.contains("03/")] = 1
matome.head()


# ## 変数名
# 
# |  |購買あり| 購買なし |
# |:-----:|:----:|:-----:|:-----:|
# | **広告見た** | a| b |
# | **広告見てない** | c| d |
# 

# In[100]:

matome["広告を見た人数"] = 0
matome["広告を見ていない人数"] = 0
matome["a"] = 0
matome["b"] = 0
matome["c"] = 0
matome["d"] = 0
matome.head()


# In[93]:

matome.tail()


# In[104]:

#広告を見た人数カウント
ad_count = []
#その中で購買した人数
a_count = []

#商品の変数名
for i in matome.index:
    main_var = buy_list[i]
    fre1_var = access_list[i]
    
    #広告見た人
    ad0_array =fre1["SampleID"][fre1[fre1_var]>=1].values.flatten()
    ad_count.append(len(ad0_array))
    
    #広告見た人のメインデータdfを作る
    a_df = pd.DataFrame(columns=main.columns)
    
    for j in ad0_array:
        #広告を見た人のメインデータdf
        df = main[main["SampleID"]==j]
        a_df = pd.concat([a_df,df],axis=0)
        
    #そのdfの中で買った人を数える
    a_count.append(len(a_df[a_df[main_var]==1]))
    
matome["広告を見た人数"] = ad_count
matome["a"] = a_count

matome["b"] = matome["広告を見た人数"]-matome["a"]

matome


# In[ ]:

#広告を見てない人数カウント
nonad_count = []
#その中で購買した人数
c_count = []

#商品の変数名
for i in matome.index:
    main_var = buy_list[i]
    fre1_var = access_list[i]
    
    #広告見てない人
    nonad0_array =fre1["SampleID"][fre1[fre1_var]==0].values.flatten()
    nonad_count.append(len(nonad0_array))
    
    #広告見てない人のメインデータdfを作る
    c_df = pd.DataFrame(columns=main.columns)
    
    for j in nonad0_array:
        #広告を見てない人のメインデータdf
        df = main[main["SampleID"]==j]
        c_df = pd.concat([c_df,df],axis=0)
        
    #そのdfの中で買った人を数える
    c_count.append(len(c_df[c_df[main_var]==1]))
    
matome["広告を見てない人数"] = nonad_count
matome["c"] = c_count

matome["d"] = matome["広告を見た人数"]-matome["c"]

matome


# In[ ]:



