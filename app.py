import os
import requests
from flask import Flask, render_template, request
from Util_Functions import (
    wind_degree_to_direction,
    unix_timestamp_to_localtime,
    convert_temperature,
)

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", "YOUR_OPENWEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}"
            f"&appid={API_KEY}"
        )
        response = requests.get(url).json()

        if response.get("cod") == 200:
            temp_c = convert_temperature(response["main"]["temp"], "K", "C")
            wind_dir = wind_degree_to_direction(response["wind"]["deg"])
            local_time = unix_timestamp_to_localtime(response["dt"])
            description = response["weather"][0]["description"].title()

            weather_data = {
                "city": city.title(),
                "temp": round(temp_c, 2),
                "wind": wind_dir,
                "time": local_time,
                "description": description,
            }
        else:
            weather_data = {"error": "City not found"}

    return render_template("index.html", data=weather_data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
