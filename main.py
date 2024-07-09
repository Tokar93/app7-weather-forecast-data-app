import streamlit as st
import plotly.express as px
from backend import get_data
st.title('Weather Forecast for the next days')
place = st.text_input('Place: ')
days = st.slider('Forecast days:', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

# Get the remperature/sky
filtered_data = get_data(place, days)

if option == 'Temperature':
    temperatures = [a['main']['temp'] for a in filtered_data]
    dates = [dict['dt_txt'] for dict in filtered_data]
    figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
    st.plotly_chart(figure)

if option == 'Sky':
    filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]