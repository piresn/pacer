import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from helpers import *

st.title('Pace predictor')

records = pd.read_csv('records.csv')

user_percentage = st.number_input('Set a speed percentage:',
    min_value=1.0, max_value=110.0, value=68.0, step=0.1)

records['User'] = records['Men'] * user_percentage/100

records = records.melt(id_vars='Distance', var_name='Group', value_name='Speed')

records['Pace'] = records['Speed'].apply(kmh_to_pace)

a = alt.Chart(records).mark_circle().encode(
    x=alt.Y('Distance', scale=alt.Scale(type="log")),
    y=alt.Y('Speed', scale=alt.Scale(type="log")),
    color='Group',
    tooltip=['Distance', 'Speed', 'Pace']
)

st.write(a)

st.write(records[records.Group == 'User'][['Distance', 'Pace']])