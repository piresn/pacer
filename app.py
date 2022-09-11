import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from helpers import *

st.title('Pace predictor')

records = pd.read_csv('records.csv')

####################################################

with st.sidebar:

    st.subheader('Recent Event')

    user_distance = st.selectbox('distance',
    ['100m', '200m', '400m', '800m', '1000m',
    '1500m', 'Mile', '2000m', '3000m', '5000m',
    '10000m', 'Half-marathon', 'Marathon', '50km', '100km'])
    
    col1, col2, col3 = st.columns(3)

    with col1:

        user_pace_hour = st.number_input('min',
        min_value=0, max_value=100, value=0, step=1)

    with col2:

        user_pace_min = st.number_input('min',
        min_value=0, max_value=30, value=5, step=1)

    with col3:
        user_pace_sec = st.number_input('sec',
        min_value=0, max_value=59, value=0, step=1)

    ## TODO change ro readout
    user_percentage = st.number_input('Set a speed percentage:',
        min_value=1.0, max_value=110.0, value=68.0, step=0.1)

####################################################

records['User'] = records['Men'] * user_percentage/100

records = records.melt(id_vars=['Event','Distance'], var_name='Group', value_name='Speed')

records['Pace'] = records['Speed'].apply(kmh_to_pace, decimals=False)

####################################################

a = alt.Chart(records).mark_circle().encode(
    x=alt.Y('Distance', scale=alt.Scale(type="log")),
    y=alt.Y('Speed', scale=alt.Scale(type="log")),
    color='Group',
    tooltip=['Distance', 'Speed', 'Pace']
)

st.altair_chart(a)

st.write(records[records.Group == 'User'][['Distance', 'Pace']])