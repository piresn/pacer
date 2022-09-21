import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from pace import Pace
from speedmodel import SpeedModel
from helpers import *

st.title('Pace predictor')

records = SpeedModel(pd.read_csv('records.csv'))

rawtable = pd.read_csv('records.csv') # TODO replace rawtable uses with SpeedModel methods

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

    UserPace = Pace()

    user_distance = rawtable.loc[rawtable['Event']==user_event]['Distance'].iat[0]

    UserPace.pace_from_distance(meters=user_distance,
                                     seconds=user_pace_sec,
                                     minutes=user_pace_min,
                                     hours=user_pace_hour)

    user_score = records.calculate_user_score(user_distance, UserPace.print(unit='secskm'))

    st.write(f'User pace: {UserPace.print()} is {round(user_score*100, 2)}% of maximum speed.')


####################################################

userpaces = records.get_proportion_pace(proportion=user_score)


####################################################

st.write(userpaces[['Event', 'Predicted Pace (min/km)', 'Predicted Time (h:m:s)']])

a = alt.Chart(userpaces).mark_circle().encode(
    x=alt.Y('Distance', scale=alt.Scale(type="log")),
    y=alt.Y('PredictedPace', scale=alt.Scale(type="log", zero=False)),
    tooltip=['Event', 'Predicted Pace (min/km)', 'Predicted Time (h:m:s)']
)

st.altair_chart(a)
