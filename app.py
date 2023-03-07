import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
sns.set_style('white')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
sns.set_style('white')
num_simulations = 40

all_stats = []

# Loop through many simulations
for i in range(num_simulations):
    sen = []
    for i in range (0,100):
        n=random.randint(668,749)/1000
        sen.append(n)
    sen = np.array(sen).round(2)
    
    sp = []
    for i in range (0,100):
        n=random.randint(774,941)/1000
        sp.append(n)
    sp = np.array(sp).round(2)
    
    prv = []
    for i in range (0,100):
        n=random.randint(10,250)/1000
        prv.append(n)
    prv = np.array(prv).round(2)
    
    
    df = pd.DataFrame(index=range(0,100), data={'sen': sen,'sp': sp,'prv':prv})

    # Back into the sales number using the percent to target rate
    df['PPV'] = (df['sen']*df['prv'])/((df['sen']*df['prv']) + ((1-df['sp'])*(1-df['prv'])))
    
    #all_stats.append([df['sen'],df['sp'],df['prv'],df['PPV']])
    #all_stats.append([df['sen'].mean(),df['sp'].mean(),df['prv'].mean(),df['PPV'].mean()])
    all_stats.append(df['PPV'])

Positive_Pred = pd.DataFrame(all_stats)
positive = Positive_Pred.transpose()
x= pd.DataFrame(positive.mean())
x.describe()
