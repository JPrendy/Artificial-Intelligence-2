#James Prendergast
#C13446122
#If you are having problems getting this work look at the anaconda file







# coding: utf-8

# In[258]:

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
get_ipython().magic('matplotlib inline')


# In[259]:

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# In[260]:

get_ipython().magic('pinfo read_csv')


# In[261]:

Location = r'C:\Users\james\notebooks\DataSet.txt'
df = pd.read_csv(Location)


# In[262]:

df


# In[263]:

Location2 = r'C:\Users\james\notebooks\featureNames.txt'
df2 = pd.read_csv(Location2,names=['Names'])


# In[ ]:




# In[264]:

df2


# In[265]:

##Sorted = df2.sort_values(['Names'], ascending=True)
##for i in range(0, 3):

sk = df2.iloc[0]
sk1 = df2.iloc[1]
sk2 = df2.iloc[2]
sk3 = df2.iloc[3]
sk4 = df2.iloc[4]
sk5 = df2.iloc[5]
sk6 = df2.iloc[6]
sk7 = df2.iloc[7]
sk8 = df2.iloc[8]
sk9 = df2.iloc[9]
sk10 = df2.iloc[10]
sk11 = df2.iloc[11] 
sk12 = df2.iloc[12]
sk13 = df2.iloc[13]
sk14 = df2.iloc[14] 
sk15 = df2.iloc[15]


# In[266]:

sk
sk1
sk2
sk3
sk4
sk5
sk6
sk7
sk8
sk9
sk10
sk11
sk12
sk13
sk14
sk15


# In[267]:

one = sk['Names']
two = sk1['Names']
three = sk2['Names']
four = sk3['Names']
five = sk4['Names']
six = sk5['Names']
seven = sk6['Names']
eight = sk7['Names']
nine = sk8['Names']
ten = sk9['Names']
eleven = sk10['Names']
twelve = sk11['Names']
thirteen = sk12['Names']
fourteen = sk13['Names']
fifteen = sk14['Names']
sixteen = sk15['Names']


# In[268]:

##one
##two


# In[269]:

Location = r'C:\Users\james\notebooks\DataSet.txt'
df = pd.read_csv(Location, names=[one, two, three, four, five, six, seven,eight,nine,ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen])


# In[270]:


df


# In[271]:

df.to_csv('/data/c13446122version1.csv')


# In[272]:

age1 = df[ "age"].min()
age2 = df[ "age"].mean()
age3 = df[ "age"].median()
age4 = df[ "age"].max()
age5 = df[ "age"].std()
age6 = df["age"].quantile(.25)
age7 = df["age"].quantile(.75)
age8 = df["age"].count()
age9 = df["age"].unique()


# In[273]:

##id1 = df[ "id"].min()
##id2 = df[ "id"].mean()
##id3 = df[ "id"].median()
##id4 = df[ "id"].max()
##id5 = df[ "id"].std()
##id6 = df["id"].quantile(.25)
##id7 = df["id"].quantile(.75)
##id8 = df["id"].count()
##id9 = df['id'].unique()
##these wont work because they are strings


# In[274]:

fn1 = df[ "fnlwgt"].min()
fn2 = df[ "fnlwgt"].mean()
fn3 = df[ "fnlwgt"].median()
fn4 = df[ "fnlwgt"].max()
fn5 = df[ "fnlwgt"].std()
fn6 = df["fnlwgt"].quantile(.25)
fn7 = df["fnlwgt"].quantile(.75)
fn8 = df["fnlwgt"].count()
fn9 = df["fnlwgt"].unique()



# In[275]:

ed1 = df[ "education-num"].min()
ed2 = df[ "education-num"].mean()
ed3 = df[ "education-num"].median()
ed4 = df[ "education-num"].max()
ed5 = df[ "education-num"].std()
ed6 = df["education-num"].quantile(.25)
ed7 = df["education-num"].quantile(.75)
ed8 = df["education-num"].count()
ed9 = df["education-num"].unique()




# In[276]:

cg1 = df[ "capital-gain"].min()
cg2 = df[ "capital-gain"].mean()
cg3 = df[ "capital-gain"].median()
cg4 = df[ "capital-gain"].max()
cg5 = df[ "capital-gain"].std()
cg6 = df["capital-gain"].quantile(.25)
cg7 = df["capital-gain"].quantile(.75)
cg8 = df["capital-gain"].count()
cg9 = df["capital-gain"].unique()




# In[277]:

cl1 = df[ "capital-loss"].min()
cl2 = df[ "capital-loss"].mean()
cl3 = df[ "capital-loss"].median()
cl4 = df[ "capital-loss"].max()
cl5 = df[ "capital-loss"].std()
cl6 = df["capital-loss"].quantile(.25)
cl7 = df["capital-loss"].quantile(.75)
cl8 = df["capital-loss"].count()
cl9 = df["capital-loss"].unique()


# In[278]:

hp1 = df[ "hours-per-week"].min()
hp2 = df[ "hours-per-week"].mean()
hp3 = df[ "hours-per-week"].median()
hp4 = df[ "hours-per-week"].max()
hp5 = df[ "hours-per-week"].std()
hp6 = df["hours-per-week"].quantile(.25)
hp7 = df["hours-per-week"].quantile(.75)
hp8 = df["hours-per-week"].count()
hp9 = df["hours-per-week"].unique()


# In[ ]:




# In[279]:

features = [one,two,three,four,five, six, seven,eight,nine,ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen]
minimum = ['string',age1, 'string', fn1, 'string', ed1, 'string', 'string', 'string', 'string', 'string', cg1, cl1, hp1, 'string', 'string']
mean = ['string', age2, 'string', fn2, 'string', ed2, 'string', 'string', 'string', 'string', 'string', cg2, cl2, hp2, 'string', 'string']
median = ['string',age3, 'string', fn3 , 'string', ed3, 'string', 'string', 'string', 'string', 'string', cg3, cl3, hp3, 'string', 'string']
Max = ['string',age4, 'string', fn4, 'string', ed4, 'string', 'string', 'string', 'string', 'string', cg4, cl4, hp4, 'string', 'string']
std = ['string',age5, 'string', fn5, 'string', ed5, 'string', 'string', 'string', 'string', 'string',  cg5, cl5, hp5, 'string', 'string']
first_quartile = ['string',age6, 'string', fn6, 'string', ed6, 'string', 'string', 'string', 'string', 'string', cg6, cl6, hp6, 'string', 'string']
third_quartile = ['string',age7, 'string', fn7, 'string', ed7, 'string', 'string', 'string', 'string', 'string', cg7, cl7, hp7, 'string', 'string']
instances = ['string',age8, 'string', fn8, 'string', ed8, 'string', 'string', 'string', 'string', 'string', cg8, cl8, hp8, 'string', 'string' ]
unique = ['string',age9, 'string', fn9, 'string', ed9, 'string', 'string', 'string', 'string', 'string', cg9, cl9, hp9, 'string', 'string' ]


# In[280]:

get_ipython().magic('pinfo zip')


# In[281]:

ca = list(zip(features,minimum, mean,median, Max, std, first_quartile, third_quartile, instances, unique))
ca


# In[282]:

df = pd.DataFrame(data = ca, columns=['features', 'minimum', 'mean','median', 'Max', 'std', 'first_quartile', 'third_quartile', 'instances', 'unique'])
df


# In[283]:

df.to_csv('/data/c13446122CONT.csv')


# In[284]:

features = [one,two,three,four,five, six, seven,eight,nine,ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen]
mode_fr = ['string',age1, 'string', fn1, 'string', ed1, 'string', 'string', 'string', 'string', 'string', cg1, cl1, hp1, 'string', 'string']
mode_pr = ['string', age2, 'string', fn2, 'string', ed2, 'string', 'string', 'string', 'string', 'string', cg2, cl2, hp2, 'string', 'string']
two_mode_fr = ['string',age3, 'string', fn3 , 'string', ed3, 'string', 'string', 'string', 'string', 'string', cg3, cl3, hp3, 'string', 'string']
two_mode_pr = ['string',age4, 'string', fn4, 'string', ed4, 'string', 'string', 'string', 'string', 'string', cg4, cl4, hp4, 'string', 'string']
pr = ['string',age5, 'string', fn5, 'string', ed5, 'string', 'string', 'string', 'string', 'string',  cg5, cl5, hp5, 'string', 'string']
instances = ['string',age8, 'string', fn8, 'string', ed8, 'string', 'string', 'string', 'string', 'string', cg8, cl8, hp8, 'string', 'string' ]


# In[285]:

get_ipython().magic('pinfo zip')


# In[286]:

ca2 = list(zip(features,mode_fr, mode_pr, two_mode_fr, two_mode_pr, pr, instances))
ca2


# In[287]:

df = pd.DataFrame(data = ca2, columns=['features', 'mode_fr', 'mode_pr', 'two_mode_fr', 'two_mode_pr', 'pr', 'instances'])
df2


# In[288]:

df.to_csv('/data/c13446122CAT.csv')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



