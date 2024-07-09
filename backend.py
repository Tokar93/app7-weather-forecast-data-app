import requests

API_KEY = 'd954e68e4bda855ed426b7fa525772b0'


def get_data(place, forecast_days=2, kind=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data = [a['main']['temp'] for a in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data

if __name__ == '__main__':
    forecast = get_data(place='Gdynia')
    print(forecast)