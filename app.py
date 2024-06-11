from flask import Flask, render_template, request
from weather import Weather
from forecast import WeatherForcast

app = Flask(__name__)


# To render Homepage
@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


# To test Weather web app with UI
@app.route('/weather', methods=['POST'])
def weather():
    if request.method == 'POST':

        city_name = request.form['city_name']

        operation = request.form['operation']

        if operation == "Today's Weather":

            result = Weather.weather(city_name)

            return render_template('results.html', result=result)

        if operation == "Weather Forecast":

            result = WeatherForcast.get_forecast(city_name)

            return render_template('results1.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
