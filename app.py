import altair as alt
import pandas as pd
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
sns.set_style('white')

st.title('Application to Calculate Positive and Negative Predictive Value of screening Tests from Sensitivity, Specificity and Prevalance')
sen_values = st.slider(
    'Select a range of Sensitivity',
    0.0, 100.0, (25.0, 75.0))
st.write('Sensitivity Values:', sen_values)

sp_values = st.slider(
    'Select a range of Specificity',
    0.0, 100.0, (25.0, 75.0))
st.write('Specificity Values:', sp_values)

pre_values = st.slider(
    'Select a range of Prevalance',
    0.0, 100.0, (25.0, 75.0))
st.write('Prevalance Values:', pre_values)


num_simulations = 10

all_stats = []

#Loop through many simulations
for i in range(num_simulations):
    sen = []
    for i in range (0,100):
        n=random.randint(sen_values)/100
        sen.append(n)
        sen = np.array(sen).round(2)
    
    sp = []
    for i in range (0,100):
        n=random.randint(sp_values)/100
        sp.append(n)
    sp = np.array(sp).round(2)
    
    prv = []
    for i in range (0,100):
        n=random.randint(pre_values)/100
        prv.append(n)
    prv = np.array(prv).round(2)
    
    
    df = pd.DataFrame(index=range(0,100), data={'sen': sen,'sp': sp,'prv':prv})

    
    df['PPV'] = (df['sen']*df['prv'])/((df['sen']*df['prv']) + ((1-df['sp'])*(1-df['prv'])))
    
    all_stats.append([df['sen'],df['sp'],df['prv'],df['PPV']])
    all_stats.append([df['sen'].mean(),df['sp'].mean(),df['prv'].mean(),df['PPV'].mean()])
    all_stats.append(df['PPV'])

Positive_Pred = pd.DataFrame(all_stats)
positive = Positive_Pred.transpose()
x= pd.DataFrame(positive.mean())
x.describe()
fig, ax = plt.subplots(figsize=(12, 10))
x.plot(kind='kde',ax=ax)
ax.text(0.45,15,'Positive Predictive Value:', fontsize = 12,color='blue',fontweight='bold')
ax.text(0.45,14,'Mean & SD: 41% & 2% ', fontsize = 12,color='red',fontweight='bold')
ax.get_legend().remove()
st.pyplot(fig)
