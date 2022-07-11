import requests
from datetime import datetime
import os


with open(r'E:\python project\openweather\openweather_api.txt') as f:
    api_key = f.read() # read the api key from file, we use the openweather to get the detail info of weather
   
latitude = 23.1291    # specify your latitude and longtitude
longtitude = 113.2644

def get_weather(api, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
    response = requests.get(url).json()
    
    retrieve_time = datetime.fromtimestamp(response['dt']) # get detail info from json file
    city_name = response['name']
    weather_desc = response['weather'][0]['description']
    temp_min = response['main']['temp_min'] - 273.15 # Kelvin to Celsius
    temp_cur = response['main']['temp'] - 273.15
    temp_max = response['main']['temp_max'] - 273.15 # Kelvin to Celsius
    humidity = response['main']['humidity']
    sunrise = datetime.fromtimestamp(response['sys']['sunrise']).strftime("%H:%M:%S")
    sunset = datetime.fromtimestamp(response['sys']['sunset']).strftime("%H:%M:%S")
   
    
    print(f"""It is {retrieve_time} right now!
You are in {city_name}
Today's weather is: {weather_desc}
Minimum temperature is: {round(temp_min,2)}
Current temperature is: {round(temp_cur,2)}
Maximum temperature is: {round(temp_max,2)}
Currnet humidity is: {humidity}
Sunrise: {sunrise}
Sunset: {sunset}
""")
    weather_info_to_file(retrieve_time, city_name, weather_desc, temp_min, temp_cur, temp_max, humidity, sunrise, sunset)

    
def weather_info_to_file(retrieve_time, city_name, weather_desc, temp_min, temp_cur, temp_max, humidity, sunrise, sunset):    
    path = r'E:\weather_report'  # specity our save path and file
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    
    date_prefix = datetime.now().strftime('%Y-%m-%d')
    weather_file = date_prefix+'_weather_report.txt'
    full_path = os.path.join(path, weather_file)
    
    with open(weather_file, 'w') as f:
        f.write((f"""It is {retrieve_time} right now!
You are in {city_name}
Today's weather is: {weather_desc}
Minimum temperature is: {round(temp_min,2)}
Current temperature is: {round(temp_cur,2)}
Maximum temperature is: {round(temp_max,2)}
Currnet humidity is: {humidity}
Sunrise: {sunrise}
Sunset: {sunset}
"""))
    print(f'weather report has been saved in {full_path}.')
 
 
if __name__ == '__main__':
    get_weather(api_key, latitude, longtitude)