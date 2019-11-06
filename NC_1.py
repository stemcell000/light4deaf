#!/usr/bin/env python
# coding: utf-8

# In[53]:


HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
The raw code for this IPython notebook is by default hidden for easier reading.
To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.''')


# In[ ]:


import pandas as pd
import numpy as np
import scipy as sp
import plotly
import plotly.figure_factory as ff
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.express as px
from IPython.core.display import display, HTML
from plotly.subplots import make_subplots
from IPython.display import display
pd.options.display.max_columns = None
pd.options.display.max_rows = None
display(HTML('<h2>1. Effectifs</h2>'))
df = pd.read_excel('/users/marc/IDV/Clinique/RHU/Statistiques/LIGHT4DEAF_Neurocognition_octobre_2019_20191021-4_FINAL_CR.xlsx')
df_type = pd.read_excel('/users/marc/IDV/Clinique/RHU/Statistiques/LIGHT4DEAF_Age_Type_20191022_2.xlsx')


# In[2]:


df = df[df["ID_VISITE"]!= 2]


# In[3]:


df_lsf = pd.read_excel('/users/marc/IDV/Clinique/RHU/Statistiques/LIGHT4DEAF_Neurocognition_LSF.xlsx')
df_lsf.dropna(inplace=True)
df_lsf = df_lsf.drop(columns=['SEXE_PATIENT', 'ID_SECONDAIRE'])


# In[4]:


df_lsf = pd.merge(df_lsf, df, on="ID_DOSSIER")


# In[8]:


df_type1 = df[df["Type"]=='Type 1']
df_type2 = df[df["Type"]=='Type 2']


# In[28]:


df_lsf_y = df_lsf[df_lsf["Interpréte LSF"]=='Oui']
df_lsf_n = df_lsf[df_lsf["Interpréte LSF"]=='Non']


# In[44]:


display(HTML('<p>Nombre de patients Usher de type 1 :  '+str(len(df_type1)) +'</p>'))


# In[43]:


display(HTML('<p>Nombre de patients Usher de type 2 :  '+str(len(df_type2)) +'</p>'))


# In[41]:


display(HTML('<p>Nombre de patients ayant eu recours à un interprète : '+str(len(df_lsf_y)) +'</p>'))


# In[42]:


display(HTML("<p>Nombre de patients n'ayant pas eu recours à un interprète : "+str(len(df_lsf_n)) +'</p>'))


# In[51]:


df = df[df["EXAMEN ENFANTS"] == 'Non']


# In[52]:


df_type = df_type.drop(columns=["ID_SECONDAIRE"])


# In[7]:


df = pd.merge(df_type, df, on="ID_DOSSIER")
df = df.drop(columns = ['EXAMEN ENFANTS'])


# In[11]:


#Tableau de Répartition des Années d'étude
study_repartition = df['nb_annees_etudes'].value_counts()
study_df = pd.DataFrame(data=study_repartition)
study_df.columns = ['Effectif']
study_df.index.name = "Nombre d'années d'études"
study_df.reset_index(inplace=True)
#Changement de type numérique pour les deux colonnes : float -> int
study_df['Effectif'] = study_df['Effectif'].astype(int)
study_df["Nombre d'années d'études"] = study_df["Nombre d'années d'études"].astype(int)


# In[12]:


#Tableau de Répartition des Années d'étude Type 1
study_repartition1 = df_type1['nb_annees_etudes'].value_counts()
study_df1 = pd.DataFrame(data=study_repartition1)
study_df1.columns = ['Effectif']
study_df1.index.name = "Nombre d'années d'études"
study_df1.reset_index(inplace=True)
#Changement de type numérique pour les deux colonnes : float -> int
study_df1['Effectif'] = study_df1['Effectif'].astype(int)
study_df1["Nombre d'années d'études"] = study_df1["Nombre d'années d'études"].astype(int)


# In[13]:


#Tableau de Répartition des Années d'étude Type 1
study_repartition1 = df_type2['nb_annees_etudes'].value_counts()
study_df2 = pd.DataFrame(data=study_repartition1)
study_df2.columns = ['Effectif']
study_df2.index.name = "Nombre d'années d'études"
study_df2.reset_index(inplace=True)
#Changement de type numérique pour les deux colonnes : float -> int
study_df2['Effectif'] = study_df2['Effectif'].astype(int)
study_df2["Nombre d'années d'études"] = study_df2["Nombre d'années d'études"].astype(int)


# In[14]:


fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=("", "Total", "", "Type 1", "", "Type 2"),
    vertical_spacing=0.14,
    specs=[[{"type": "table"}, {"type": 'bar'}],
           [{"type": "table"}, {"type": 'bar'}],
           [{"type": "table"}, {"type": 'bar'}]]
)


# In[15]:


fig.add_trace(
    go.Table(
    header=dict(values=["Nombre d'années<br>d'études", "Effectif"],
                font=dict(size=10),
                align='left'),
    cells=dict(values=[study_df[k].tolist() for k in study_df.columns[0:]], align = "left"))
, row=1, col=1)

fig.add_trace(
    go.Bar(x=study_df["Nombre d'années d'études"], y=study_df["Effectif"])
, row=1, col=2)


fig.add_trace(
    go.Table(
    header=dict(values=["Nombre d'années<br>d'études", "Effectif (Type1)"],
                font=dict(size=10),
                align='left'),
    cells=dict(values=[study_df1[k].tolist() for k in study_df1.columns[0:]], align = "left"))
, row=2, col=1)

fig.add_trace(
    go.Bar(x=study_df1["Nombre d'années d'études"], y=study_df1["Effectif"])
, row=2, col=2)

fig.add_trace(
    go.Table(
    header=dict(values=["Nombre d'années<br>d'études", "Effectif (Type1)"],
                font=dict(size=10),
                align='left'),
    cells=dict(values=[study_df2[k].tolist() for k in study_df2.columns[0:]], align = "left"))
, row=3, col=1)

fig.add_trace(
    go.Bar(x=study_df2["Nombre d'années d'études"], y=study_df2["Effectif"])
, row=3, col=2)


fig.update_xaxes(title_text="Nombre d'années d'études", row=1, col=2)
fig.update_yaxes(title_text="Effectif", row=1, col=2)
fig.update_xaxes(title_text="Nombre d'années d'études", row=2, col=2)
fig.update_yaxes(title_text="Effectif", row=2, col=2)
fig.update_xaxes(title_text="Nombre d'années d'études", row=3, col=2)
fig.update_yaxes(title_text="Effectif", row=2, col=2)

fig.update_layout(
    height=800,
    showlegend=False,
    title_text="Répartition du nombre d'années d'études",
)


# In[16]:


#Tableau de répartition des professions
#Fréquences
job_repartition = df['Profession'].value_counts()
#DataFrame
job_df = pd.DataFrame(data=job_repartition)
#Renommage de colonne
job_df.columns = ['Effectif']
#Index nommé 'Profession'
job_df.index.name = "Profession"
#transformé en colonne de données
job_df.reset_index(inplace=True)

#Tableau de répartition des professions Type 1
#Fréquences
job_repartition1 = df_type1['Profession'].value_counts()
#DataFrame
job_df1 = pd.DataFrame(data=job_repartition1)
#Renommage de colonne
job_df1.columns = ['Effectif']
#Index nommé 'Profession'
job_df1.index.name = "Profession"
#transformé en colonne de données
job_df1.reset_index(inplace=True)

#Tableau de répartition des professions Type 1
#Fréquences
job_repartition2 = df_type2['Profession'].value_counts()
#DataFrame
job_df2 = pd.DataFrame(data=job_repartition2)
#Renommage de colonne
job_df2.columns = ['Effectif']
#Index nommé 'Profession'
job_df2.index.name = "Profession"
#transformé en colonne de données
job_df2.reset_index(inplace=True)


# In[17]:


fig_job = make_subplots(
    rows=3, cols=2,
    subplot_titles=("", "Total", "", "Type 1", "", "Type 2"),
    vertical_spacing=0.2,
    specs=[[{"type": "table"}, {"type": 'bar'}],
           [{"type": "table"}, {"type": 'bar'}],
           [{"type": "table"}, {"type": 'bar'}]]
)


# In[18]:


fig_job.add_trace(
    go.Table(
    header=dict(values=["Profession", "Effectif"],
                font=dict(size=10),
                align='left'),
    cells=dict(values=[job_df[k].tolist() for k in job_df.columns[0:]], align = "left"))
, row=1, col=1)

fig_job.add_trace(
    go.Bar(x=job_df["Profession"], y=job_df["Effectif"])
, row=1, col=2)


fig_job.add_trace(
    go.Table(
    header=dict(values=["Profession", "Effectif (Type1)"],
                font=dict(size=10),
                align='left'),
    cells=dict(values=[job_df1[k].tolist() for k in job_df1.columns[0:]], align = "left"))
, row=2, col=1)

fig_job.add_trace(
    go.Bar(x=job_df1["Profession"], y=job_df1["Effectif"])
, row=2, col=2)

fig_job.add_trace(
    go.Table(
    header=dict(values=["Profession", "Effectif (Type1)"],
                font=dict(size=10),
                align='left'),
    cells=dict(values=[job_df2[k].tolist() for k in job_df2.columns[0:]], align = "left"))
, row=3, col=1)

fig_job.add_trace(
    go.Bar(x=job_df2["Profession"], y=job_df2["Effectif"])
, row=3, col=2)


fig_job.update_yaxes(title_text="Effectif", row=1, col=2)
fig_job.update_yaxes(title_text="Effectif", row=2, col=2)
fig_job.update_yaxes(title_text="Effectif", row=3, col=2)

fig_job.update_layout(
    height=1200,
    showlegend=False,
    title_text="Répartition des professions",
)

