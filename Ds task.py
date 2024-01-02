import pandas as pd
import requests


# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Function to create a CSV dataset
def create_csv_dataset(api_key, city_list):
    data_list = []

    for city in city_list:
        weather_data = get_weather_data(api_key, city)
        
        if weather_data:
            data = {
                'City': city,
                'Temperature (Celsius)': weather_data['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
                'Humidity (%)': weather_data['main']['humidity'],
                'Description': weather_data['weather'][0]['description'],
            }
            data_list.append(data)

    # Create a Pandas DataFrame
    df = pd.DataFrame(data_list)

    # Save the DataFrame to a CSV file
    df.to_csv('weather_dataset.csv', index=False)
    print("CSV dataset created successfully.")

# Example usage
api_key = "https://home.openweathermap.org/myservices"
cities = ["London", "New York", "Tokyo", "Sydney"]

create_csv_dataset(api_key, cities)
