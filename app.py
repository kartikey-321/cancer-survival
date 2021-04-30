from flask import Flask,render_template,redirect,request
import joblib
import numpy as np
import pandas as pd


model=joblib.load('cricket.pkl')

app=Flask(__name__)


df=pd.read_csv('cricket.csv')
df=df[df['overs']>=5]

cols=df.columns

bat=df['bat_team'].unique().tolist()
bowl=df['bowl_team'].unique().tolist()




@app.route('/')
def hello():
    return render_template('index.html',cols=cols,bat=bat,bowl=bowl)


@app.route('/home')
def home():
    return redirect('/')



@app.route('/',methods=['POST'])
def submit():
    if request.method=='POST':
        bat=request.form['bat']
        if bat=='Bangladesh':
            bat_bangladesh=1
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Canada':
            bat_bangladesh=0
            bat_canada=1
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='England':
            bat_bangladesh=0
            bat_canada=0
            bat_england=1
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Hong Kong':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=1
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='India':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=1
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Ireland':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=1
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Kenya':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=1
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Netherlands':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=1
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='New Zealand':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=1
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Pakistan':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=1
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Scotland':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=1
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='South Africa':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=1
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='Sri Lanka':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=1
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='United Arab Emirates':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=1
            bat_westindies=0
            bat_zimbabwe=0
        elif bat=='West Indies':
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=1
            bat_zimbabwe=0
        else:
            bat_bangladesh=0
            bat_canada=0
            bat_england=0
            bat_hongkong=0
            bat_india=0
            bat_ireland=0
            bat_kenya=0
            bat_netherland=0
            bat_newzealand=0
            bat_pakistan=0
            bat_scotland=0
            bat_southafrica=0
            bat_srilanka=0
            bat_uae=0
            bat_westindies=0
            bat_zimbabwe=1
        
        bowl=request.form['bowl']
        if bowl=='Bangladesh':
            bowl_bangladesh=1
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Canada':
            bowl_bangladesh=0
            bowl_canada=1
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='England':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=1
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Hong Kong':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=1
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='India':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=1
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Ireland':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=1
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Kenya':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=1
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Netherlands':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=1
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='New Zealand':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=1
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Pakistan':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=1
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Scotland':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=1
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='South Africa':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=1
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='Sri Lanka':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=1
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='United Arab Emirates':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=1
            bowl_westindies=0
            bowl_zimbabwe=0
        elif bowl=='West Indies':
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=1
            bowl_zimbabwe=0
        else:
            bowl_bangladesh=0
            bowl_canada=0
            bowl_england=0
            bowl_hongkong=0
            bowl_india=0
            bowl_ireland=0
            bowl_kenya=0
            bowl_netherland=0
            bowl_newzealand=0
            bowl_pakistan=0
            bowl_scotland=0
            bowl_southafrica=0
            bowl_srilanka=0
            bowl_uae=0
            bowl_westindies=0
            bowl_zimbabwe=1
        
        
        over=float(request.form['over'])
        runs=int(request.form['runs'])
        wickets=int(request.form['wickets'])
        runs_5=int(request.form['runs_5'])
        wickets_5=int(request.form['wickets_5'])
        

        result=model.predict([[
            runs,
            wickets,
            over,
            runs_5,
            wickets_5,
            bat_bangladesh,
            bat_canada,
            bat_england,
            bat_hongkong,
            bat_india,
            bat_ireland,
            bat_kenya,
            bat_netherland,
            bat_newzealand,
            bat_pakistan,
            bat_scotland,
            bat_southafrica,
            bat_srilanka,
            bat_uae,
            bat_westindies,
            bat_zimbabwe,
            bowl_bangladesh,
            bowl_canada,
            bowl_england,
            bowl_hongkong,
            bowl_india,
            bowl_ireland,
            bowl_kenya,
            bowl_netherland,
            bowl_newzealand,
            bowl_pakistan,
            bowl_scotland,
            bowl_southafrica,
            bowl_srilanka,
            bowl_uae,
            bowl_westindies,
            bowl_zimbabwe
        ]])
        result=result[0]
        value=int(result)
    return render_template('index.html',result=value)



if __name__=='__main__':
    app.run(debug=True)