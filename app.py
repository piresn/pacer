import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from pace import Pace
from speedmodel import SpeedModel
from helpers import *

st.title('Pace predictor')

records_data = pd.read_csv('records.csv')
model = SpeedModel(records_data)
distance_map = dict(zip(records_data['Event'], records_data['Distance']))


####################################################

with st.sidebar:

    st.subheader('Recent Event')

    user_event = st.selectbox('distance',
                              ['100m', '200m', '400m', '800m', '1000m',
                               '1500m', 'Mile', '2000m', '3000m', '5000m',
                               '10000m', 'Half-marathon', 'Marathon', '50km', '100km'],
                               index=4)

    col1, col2, col3 = st.columns(3)

    with col1:

        user_pace_hour = st.slider('hour',
                                         min_value=0, max_value=12, value=0, step=1)

    with col2:

        user_pace_min = st.slider('min',
                                        min_value=0, max_value=59, value=5, step=1)

    with col3:
        user_pace_sec = st.slider('sec',
                                        min_value=0, max_value=59, value=0, step=1)



####################################################


    user_distance = distance_map[user_event]

    UserPace = Pace(meters=user_distance,
                    seconds=user_pace_sec,
                    minutes=user_pace_min,
                    hours=user_pace_hour)

    user_score = model.calculate_user_score(user_distance, UserPace)

    st.write(f'User pace: {UserPace.print()} is {model.print_user_score()}% of maximum speed.')


####################################################

predict_method = st.radio('Select model', options=['Nuno', 'Riegel standard', 'Riegel elite'], index=1, horizontal = True)
userpaces = model.predict_paces(predict_method)

st.write(userpaces[['Event', 'Predicted Pace (min/km)', 'Predicted Time (h:m:s)']])

a = alt.Chart(userpaces).mark_circle().encode(
    x=alt.Y('Distance', scale=alt.Scale(type="log")),
    y=alt.Y('PredictedPace', scale=alt.Scale(type="log", zero=False)),
    tooltip=['Event', 'Predicted Pace (min/km)', 'Predicted Time (h:m:s)']
)

st.altair_chart(a)
