
# coding: utf-8

# In[13]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.plotly as py
import plotly.graph_objs as go
data=pd.read_csv('F:\\project\\Data set\\Project Final Code\\ReposData.csv',encoding='latin-1')
data['Created_at']
#print(data)
#date=data.iloc[:,2]
#print(date)
data['Created_at']=pd.to_datetime(data['Created_at'])#,format='%Y-%m-%dT%H:%M:%SZ')
#print(data['Created_at'])
#print(data[data['created_at'].isnull()])
data['Created_at'] = pd.to_datetime(data['Created_at'],errors = 'ignore')
data['year'], data['month'] = data['Created_at'].dt.year, data['Created_at'].dt.month
#print(data['year'])


# In[37]:


def Visual_lang_on_year(parameter):
    for i in data['year']:
        if (parameter == i):
            lang=data.groupby(['Language','year'])['Language'].size()#.get_group((2009,'C')).count()
            lang1=lang.unstack()[parameter].plot(kind='bar',color="blue",fontsize=13,figsize=(20,5))
            plt.title("Most Prominent Programming language in {0}".format(parameter),fontsize=20)
            lang1.set_alpha(0.8)
            plt.rc('xtick.major', size=5)
            plt.xlabel('Languages',fontsize=14,fontweight='bold')
            plt.ylabel('Total Number of Repos',fontsize=14,fontweight='bold')
            plt.show()
            break
            
year=int(input('Enter the Year: '))
Visual_lang_on_year(year)


# In[32]:


def year_wise_lang_visual(parameter):
        for i in data['Language']:
            if (parameter == i):
                lang=data.groupby(['year','Language'])['year'].size()#.get_group((2009,'C')).count()
                lang.unstack()[parameter].plot(kind='barh',color="orange",fontsize=13,figsize=(20,5))#(figsize=(20,10), linewidth=5, fontsize=20)#.bar(figsize=(20,5))
                plt.title('Number of Repos Belong to {0} in Each Year'.format(parameter),fontsize=24)
                ax = plt.gca()
                ax.grid(True)
                plt.xlabel('Total Repos',fontsize=14,fontweight='bold')
                plt.ylabel('Year',fontsize=14,fontweight='bold')
                #py.iplot(new)
                #plt.show()
                break

lang_input=str(input('Enter the  Programming Language: '))
year_wise_lang_visual(lang_input)


# In[39]:


def Prominent_Language():
        data.groupby('Language')['year'].count().plot(kind='bar',color="red",fontsize=13,figsize=(20,5))
        plt.title("Most Prominent Programming language ",fontsize=20)
        plt.xlabel("Language",fontsize=14,fontweight='bold')
        plt.ylabel("Popular Language",fontsize=14,fontweight='bold')
        plt.show()
Prominent_Language()


# In[8]:


def Top_Five_Language():
        colors = ['#FF0000', '#00ff00', '#00ffbf', '#ffff00', '#0000ff']
        explode = (0.1, 0, 0, 0,0)
        data.groupby('Language')['year'].count().sort_values(ascending=False).head(5).plot.pie(colors=colors,autopct='%1.0f%%')#(kind='pie',figsize=(20,5))
        my_circle=plt.Circle( (0,0), 0.7, color='white')
        p=plt.gcf()
        p.gca().add_artist(my_circle)
        plt.title("Top 5 Programming Language",fontsize=20)
        #plt.xlabel('Year',fontsize=14,fontweight='bold')
        plt.ylabel('')
        #plt.ylabel("Popular Language",fontweight='bold')
        plt.legend( title="Language",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
        plt.show()
Top_Five_Language()

