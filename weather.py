import http.client
import json
from API import base_url_for_current_weather, API_Key

base_url = base_url_for_current_weather


class Weather:
    @staticmethod
    def weather(city_name):

        complete_url = f"{base_url}?q={city_name}&appid={API_Key}&units=metric"

        conn = http.client.HTTPConnection("api.openweathermap.org")

        conn.request("GET", complete_url)

        response = conn.getresponse()

        data = response.read()

        x = json.loads(data)

        if x["cod"] != "404":

            y = x["main"]
            z = x["wind"]

            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            wind_speed = z["speed"]

            description = x["weather"]
            weather_description = description[0]["description"]

            result = f"Temperature (in Celsius unit) = {current_temperature}°C\n"
            result += f"Atmospheric pressure (in hPa unit) = {current_pressure} hPa\n"
            result += f"Humidity (in percentage) = {current_humidity}%\n"
            result += f"Wind speed (in km/h) = {wind_speed} km/h\n"
            result += f"Description = {weather_description}"

        else:
            result = f"City '{city_name}' Not Found"

        conn.close()

        return result
