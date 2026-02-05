import requests
import json
import time

eu_capitals = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    {"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague", "country": "Czechia", "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki", "country": "Finland", "lat": 60.1695, "lon": 24.9354},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
    {"city": "Valletta", "country": "Malta", "lat": 35.8989, "lon": 14.5146},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]

# Helper function to give names to weather codes
def get_weather_string(code):
    # WMO Weather interpretation codes 
    if code == 0: return "Clear sky"
    if code in [1, 2, 3]: return "Mainly clear, partly cloudy, and overcast"
    if code in [45, 48]: return "Fog"
    if code in [51, 53, 55]: return "Drizzle"
    if code in [61, 63, 65]: return "Rain"
    if code in [71, 73, 75]: return "Snow fall"
    if code in [80, 81, 82]: return "Rain showers"
    if code in [95, 96, 99]: return "Thunderstorm"
    return "Unknown"

final_data = {}

print("Starting weather data collection..")

for cap in eu_capitals:
    city_name = cap["city"]
    print(f"Fetching data for {city_name}..")
    
    try:
        # Setting up the API parameters
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": cap["lat"],
            "longitude": cap["lon"],
            "current_weather": "true",
            "hourly": "temperature_2m,precipitation_probability,weathercode",
            "forecast_days": 1  # We only need the current day
        }
        
        # Making the request
        response = requests.get(url, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Processing current weather
            current = data["current_weather"]
            weather_desc = get_weather_string(current["weathercode"])
            
            # Processing hourly data
            hourly_list = []
            hourly_raw = data["hourly"]
            
            # The API returns lists for each variable, so we have to zip them together
            # Loops through the 24 hours 
            for i in range(len(hourly_raw["time"])):
                hour_item = {
                    "time": hourly_raw["time"][i],
                    "temperature": hourly_raw["temperature_2m"][i],
                    "precipitation_probability": hourly_raw["precipitation_probability"][i],
                    "weathercode": hourly_raw["weathercode"][i]
                }
                hourly_list.append(hour_item)
            
            # Building the dictionary structure
            city_entry = {
                "country": cap["country"],
                "coordinates": {
                    "latitude": cap["lat"],
                    "longitude": cap["lon"]
                },
                "current_weather": {
                    "temperature": current["temperature"],
                    "windspeed": current["windspeed"],
                    "weathercode": current["weathercode"],
                    "condition": weather_desc,
                    "time": current["time"]
                },
                "hourly_forecast": hourly_list
            }
            
            # Add to our main dictionary
            final_data[city_name] = city_entry
            
        else:
            print(f"Error: API returned status code {response.status_code} for {city_name}")

    except Exception as e:
        # Log error but keep going
        print(f"Failed to get data for {city_name}. Error: {e}")

    # Small delay to be nice to API
    time.sleep(1)

# Saveto JSON file
print("Saving data to eu_weather_data.json...")
with open("eu_weather_data.json", "w") as f:
    json.dump(final_data, f, indent=4)

print("Done!")