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


num_simulations = 100

all_stats_ppv = []
all_stats_npv = []

#Loop through many simulations
for i in range(num_simulations):
    sen = []
    for i in range (0,100):
        n=random.randint(int(sen_values[0]),int(sen_values[1]))/100
        sen.append(n)
    sen = np.array(sen).round(2)
    
    sp = []
    for i in range (0,100):
        n=random.randint(int(sp_values[0]),int(sp_values[1]))/100
        sp.append(n)
    sp = np.array(sp).round(2)
    
    prv = []
    for i in range (0,100):
        n=random.randint(int(pre_values[0]),int(pre_values[1]))/100
        prv.append(n)
    prv = np.array(prv).round(2)
    
    
    df = pd.DataFrame(index=range(0,100), data={'sen': sen,'sp': sp,'prv':prv})
    df['PPV'] = (df['sen']*df['prv'])/((df['sen']*df['prv']) + ((1-df['sp'])*(1-df['prv'])))
    df['NPV'] = (df['sp']*(1-df['prv']))/(((1-df['sen'])*df['prv']) + ((df['sp'])*(1-df['prv'])))
    all_stats_ppv.append(df['PPV'])
    all_stats_npv.append(df['NPV'])
    
Positive_Pred = pd.DataFrame(all_stats_ppv)
Negative_Pred = pd.DataFrame(all_stats_npv)
positive = Positive_Pred.transpose()
negative = Negative_Pred.transpose()
x= pd.DataFrame(positive.mean())
y= pd.DataFrame(negative.mean())
fig, ax = plt.subplots(1,2,figsize=(10, 4))
sns.kdeplot(x.squeeze(),ax=ax[0],color='green').set(xlabel='Positive Predictive Value')
sns.kdeplot(y.squeeze(),ax=ax[1],color='crimson').set(xlabel='Negative Predictive Value')    
st.pyplot(fig)
