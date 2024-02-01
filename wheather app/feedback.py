import requests
from flask import Flask, render_template, request

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST']) 
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        wheather_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key=LA3V6GWJCTBDGMJWWXF5NUWWN&contentType=json'
        wheather_data = requests.get(wheather_url).json()

        # extract relevant weather data from API response
        address = wheather_data['address']
        windspeed = wheather_data['days'][1]['windspeed']
        description = wheather_data['description']
        temp = wheather_data['days'][0]['temp']
        datetime = wheather_data['days'][0]['datetime']
        resolvedAddress=wheather_data['resolvedAddress']
        humidity=wheather_data['currentConditions']['humidity']

        

        return render_template('wheather.html', address=address,windspeed=windspeed,description=description,temp=temp,
                               datetime=datetime,resolvedAddress=resolvedAddress,humidity=humidity)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
