import requests

def get_weather(city):
    geo_response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }
    )
    
    geo_data = geo_response.json()
    
    if "results" not in geo_data:
        return f"Could not find the city {city}"
    
    location = geo_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]
    
    weather_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,weather_code"
        }
    )
    
    weather_data = weather_response.json()
    temperature = weather_data["current"]["temperature_2m"]
    weather_code = weather_data["current"]["weather_code"]
    
    return {
        "city": city,
        "temperature": temperature,
        "weather_code": weather_code
    }

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city"
                }
            },
            "required": ["city"]
        }
    }
]