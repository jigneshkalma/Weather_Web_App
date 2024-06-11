from flask import Flask, render_template, request
from weather import Weather

app = Flask(__name__)


# To render Homepage
@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


# To test Weather web app with Postman
@app.route('/via_postman', methods=['POST'])
def weather_testing_with_postman():
    if request.method == 'POST':

        city_name = request.json['city_name']  # Use request.json instead of request.form for testing from postman

        result = Weather.weather(city_name)

    return result

if __name__ == '__main__':
    app.run(debug=True)
