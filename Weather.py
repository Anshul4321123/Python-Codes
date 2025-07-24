import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  
    }

    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        
        print(f"\n🌍 Weather in {city_name.title()}:")
        print(f"Condition: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Error: City not found or invalid API key.")

api_key = "YOUR_API_KEY_HERE"


city = input("Enter city name: ")
get_weather(city, api_key)
