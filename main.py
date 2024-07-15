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

if place:
    try:
        # Get the temperature/sky
        filtered_data = get_data(place, days)

        # Create temperatures and dates and plot them
        if option == 'Temperature':
            temperatures = [a['main']['temp'] / 10 for a in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            for image, date in zip(image_paths, dates):
                st.image(image, width=115)
                st.text(date)
    except KeyError:
        st.info('The location does not exist. Try again', icon=":material/cancel:")