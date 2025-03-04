import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('search-for-happiness/happy.csv')
cols = list(df.columns)
cols_format = [col.replace('_', ' ').title() for col in cols]
gdp_index = cols_format.index('Gdp')
cols_format[gdp_index] = "GDP"
cols_tuple = tuple(cols_format)

cols_dict = {}
for col_format, col in zip(cols_format, cols):
        cols_dict[col_format] = col

st.title('In Search for Happiness')

x_axis = st.selectbox('Select the data for X-axis', options=cols_tuple)
y_axis = st.selectbox('Select the data for Y-axis', options=cols_tuple)
st.subheader(f'{x_axis} and {y_axis}')

fig = px.scatter(x=df[cols_dict[x_axis]], y=df[cols_dict[y_axis]], labels={'x': x_axis, 'y': y_axis})
st.plotly_chart(fig)