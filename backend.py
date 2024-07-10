import requests

API_KEY = 'd954e68e4bda855ed426b7fa525772b0'


def get_data(place, forecast_days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    forecast = get_data(place='Gdynia', forecast_days=3)
    print(forecast)