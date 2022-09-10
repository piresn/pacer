import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from helpers import *

st.title('Pace predictor')

records = pd.read_csv('records.csv')

records = records.melt(id_vars='Distance', var_name='Gender', value_name='Speed')

records['Pace'] = records['Speed'].apply(kmh_to_pace)


a = alt.Chart(records).mark_circle().encode(
    x=alt.Y('Distance', scale=alt.Scale(type="log")),
    y=alt.Y('Speed', scale=alt.Scale(type="log")),
    color='Gender',
    tooltip=['Distance', 'Speed', 'Pace']
)

st.write(a)