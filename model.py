import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
df=pd.read_csv('./cricket.csv')
df=df[df['overs']>=5]
one_hot=df[['bat_team']+['bowl_team']]
one_hot=pd.get_dummies(one_hot,drop_first=True)
df=df.drop(columns=['bat_team','bowl_team'])
df=pd.concat([df,one_hot],axis=1)
y=df[['total']]
x=df.drop(columns=['total'])
x=x.values
y=y.values
x,xt,y,yt=train_test_split(x,y,random_state=1)
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor()
rf.fit(x,y)
joblib.dump(rf,'cricket.pkl')