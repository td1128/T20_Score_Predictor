import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np

pipe=pk.load(open('pipe.pkl','rb'))
teams=[
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afganistan',
    'Pakistan',
    'Sri Lanka'
]
cities=['Colombo',
 'Dubai',
 'Johannesburg',
 'Auckland',
 'Barbados',
 'London',
 'Pallekele',
 'Cape Town',
 'Mirpur',
 'Sydney',
 'Melbourne',
 'St Lucia',
 'Nottingham',
 'Abu Dhabi',
 'Hamilton',
 'Lauderhill',
 'Centurion',
 'Manchester']

st.title('T20 Score Predictor')

col1,col2 =st.columns(2)
with col1:
    batting_team=st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('Select bowling team',sorted(teams))

city=st.selectbox('Select City',sorted(cities))

col3,col4,col5 =st.columns(3)

with col3:
    current_score=st.number_input('Current Score')
with col4:
    overs=st.number_input('Overs done(minimum 5 overs)')
with col5:
    wickets=st.number_input('Wickets taken')

last_five_overs=st.number_input('Runs scored in last five overs')



if st.button('Predict Score'):
    balls_left =120-(overs*6)
    wickets_left =10-wickets
    crr=current_score/overs
    input_df=pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'current_score':[current_score],
        'balls_left':[balls_left],
        'wickets_left':[wickets_left],
        'crr':[crr],
        'last_five':[last_five_overs]     
    })
    # st.table(input_df)
    result=pipe.predict(input_df)
    st.hear("Predicted Score is :"+str(int(result[0])))