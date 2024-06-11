import json
import http.client
from API import base_url_for_weather_forecast, API_Key

BASE_URL = base_url_for_weather_forecast


class WeatherForcast:
    @staticmethod
    def get_forecast(city_name):

        # Construct the complete URL for the API request
        complete_url = f"{BASE_URL}?q={city_name}&appid={API_Key}&units=metric"

        # Make the API request
        conn = http.client.HTTPConnection("api.openweathermap.org")

        conn.request("GET", complete_url)

        # Get the response
        response = conn.getresponse()

        data = response.read()

        # Parse the JSON response
        data = json.loads(data)

        # Check if the city is found
        if data["cod"] != "404":

            forecasts = data["list"]
            city_info = data["city"]

            # Extract relevant forecast data
            forecast_data = []

            for forecast_item in forecasts:

                forecast_info = {
                    "date_time": forecast_item["dt_txt"],
                    "temperature": forecast_item["main"]["temp"],
                    "pressure": forecast_item["main"]["pressure"],
                    "humidity": forecast_item["main"]["humidity"],
                    "weather_description": forecast_item["weather"][0]["description"],
                    "wind_speed": forecast_item["wind"]["speed"]
                }

                forecast_data.append(forecast_info)

            # Prepare the result to be displayed
            result = {
                    "city": city_info["name"],
                    "country": city_info["country"],
                    "forecasts": forecast_data
                }

        else:
            result = {"error": f"City '{city_name}' Not Found"}

            conn.close()

        return result
