from crypt import methods
from flask import Flask, render_template, request
import requests
import datetime
import pytz

app = Flask(__name__)

@app.route("/kaset_sombun", methods=["GET"])
def index():

    api_key = "c53e332dc516ab13f41651cb872a1a4e"

    city_name = "kaset sombun"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city_name,api_key)
    data = requests.get(url).json()
    time_zone = pytz.timezone("ASIA/BANGKOK")
    date_time = datetime.datetime.now(time_zone).strftime("%d.%m.%Y - %H.%M")
    
    #dt = data["dt"]
    #date_time = datetime.datetime.fromtimestamp(dt).strftime("%d.%m.%Y - %H.%M")

    description = data["weather"][0]["description"]
    temp = round(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    

    return render_template("index.html", date_time=date_time,description=description,temp=temp,humidity=humidity,wind=wind)

if __name__ == "__main__":
    app.run(debug=True)
