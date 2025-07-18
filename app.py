import altair as alt
import pandas as pd
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
sns.set_style('white')

st.title('Calculation of Positive and Negative Predictive Value of Screening Tests from a range of Sensitivity, Specificity and Disease Prevalence')
st.subheader(':red[Monte Carlo Simulation Approach]')
st.subheader(':blue[@Designed and Developed by Dr. Arkaprabha Sau,MBBS, MD (Gold Medalist), PhD (Computer Science and Engineering)]')
st.header('Please specify the range of Sensitivity, Specificity of the Test and Prevalence of the Disease')
st.success('Sensitivity')
sen_values = st.slider(
    'Select a range of Sensitivity',
    0.0, 100.0, (25.0, 75.0))
st.write('Sensitivity Values:', sen_values)
st.warning("Specificity")
sp_values = st.slider(
    'Select a range of Specificity',
    0.0, 100.0, (25.0, 75.0))
st.write('Specificity Values:', sp_values)
st.error("Prevalence")
pre_values = st.slider(
    'Select a range of Prevalence',
    0.0, 100.0, (25.0, 75.0))
st.write('Prevalence Values:', pre_values)


num_simulations = 50

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

st.info("Result based on Simulation")
st.subheader('Mean and Standard Deviation of the Positive Predictive Value (%)')
st.write('Mean',x.mean()*100)
st.write("Standard Deviation",x.std()*100)
st.subheader('Mean and Standard Deviation of the Negative Predictive Value (%)')
st.write('Mean',y.mean()*100)
st.write("Standard Deviation",y.std()*100)

st.subheader('Distribution of the Positive and Negative Predictive Value')
fig, ax = plt.subplots(1,2,figsize=(12, 6))
sns.kdeplot(x.squeeze(),ax=ax[0],color='green',fill=True).set(xlabel='Positive Predictive Value')
sns.kdeplot(y.squeeze(),ax=ax[1],color='crimson',fill=True).set(xlabel='Negative Predictive Value')    
st.pyplot(fig)
