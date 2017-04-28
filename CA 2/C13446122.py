
# coding: utf-8

# In[444]:

#Artificial Intelligence Continuous Assessment 2
#James Prendergast
#C13446122
#21/04/2017

# Import all libraries needed for this Assessment

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


# In[445]:

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# In[446]:

#this function is used to read files
get_ipython().magic('pinfo read_csv')


# In[447]:

#this retrieves the "queries.txt" file from the sub directory from the folder data
Location = r'C:/data/queries.txt'
df = pd.read_csv(Location)


# In[448]:

#this is calling of the dataframe called df
df


# In[449]:

#this retrieves the "datadescription.txt" file from the sub directory from the folder data
Location2 = r'C:/data/datadescription.txt'
df2 = pd.read_csv(Location2,names=['Names'])


# In[450]:

#this calls the dataframe again, but it is now called df2
df2


# In[451]:

#for this we are assigning the values from "datadescription.txt" in their own values
#so they can used as header information
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
sk16 = df2.iloc[16] 
sk17 = df2.iloc[17]


# In[452]:

#this was used to check all the value worked and they stored the information from "datadescription.txt"
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
sk16
sk17


# In[453]:

#the values are assigned again to make it easier to manage
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
seventeen = sk16['Names']
eighteen = sk15['Names']


# In[454]:

# Always display all the columns
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60) 


# In[455]:

#this calls to read from the file "queries.txt" again from the sub-directory data now with the header we have assigned
Location = r'C:/data/queries.txt'
df = pd.read_csv(Location, names=[one, two, three, four, five, six, seven,eight,nine,ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen])


# In[456]:

#this calls the dataframe now with the added headers
df


# In[457]:

#this writes the solution to a file in a subdirectory called "solution", in this directory the file "C13446122.txt" is created
#this is only for temporary to make sure it was saved correctly
df.to_csv('/solution/C13446122.txt')


# In[458]:

#this will show the first five values from the dataframe to quickly check
df[:5]


# In[459]:

#this will create a new column called "Outlier", this was needed as I had problems creating other column when I commented this out 
df['Outlier'] = True
df


# In[460]:

#we create a new dataframe called newdf and copies everything from df
newdf = df.copy()
#we are creating a new dataframe called Prediction, this is where we will be using the data classifier to help make our predictions
# for this in the columnn Prediction, we call True everything an id had education of tertiary.
#this was used as the predictions as we can assume people who had a higher education has higher chances in life and will
#used to represent predictions
newdf['Prediction'] = abs(newdf['5 - education (categorical: "unknown"'] == "tertiary")
#this calls the datafram newdf
newdf                       


# In[461]:

#for this we are replacing the true and false values in the Prediction column with TypeA and TypeB, this
#data will be used to make our predictions
newdf
newdf['Prediction'].replace(True, 'TypeA',inplace=True)
newdf['Prediction'].replace(False, 'TypeB',inplace=True)
newdf


# In[462]:

#for this we are creating a new dataframe based on the columns of id and predictions and then calling
#the dataframe
test_ed = newdf[['1 - id','Prediction']]
test_ed


# In[463]:

#this new dataframe is then written and saved to a text file in a sub-directory called "solution"
test_ed.to_csv('/solution/C13446122.txt')


# In[192]:




# In[ ]:




# In[ ]:




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



