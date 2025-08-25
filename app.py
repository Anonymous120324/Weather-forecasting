import os
import requests
from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)

API_KEY = "PUSH_YOUR_API_KEY_HERE" 


def get_weather(city):
    """Fetch current weather + 5-day forecast for a given city."""
    base_url = "http://api.openweathermap.org/data/2.5/"
    weather_url = f"{base_url}weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"{base_url}forecast?q={city}&appid={API_KEY}&units=metric"

    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code != 200 or forecast_response.status_code != 200:
        return None, None

    weather_data = weather_response.json()
    forecast_data = forecast_response.json()

    # Current weather
    current_weather = {
        "city": weather_data["name"],
        "temp": weather_data["main"]["temp"],
        "humidity": weather_data["main"]["humidity"],
        "wind": weather_data["wind"]["speed"],
        "condition": weather_data["weather"][0]["description"].title(),
        "icon": weather_data["weather"][0]["icon"],
    }

    # Forecast (1 reading per day at 12:00)
    forecast_list = []
    daily_temps = []
    daily_dates = []

    for item in forecast_data["list"]:
        if "12:00:00" in item["dt_txt"]:
            forecast_list.append({
                "date": datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%a, %d %b"),
                "min": item["main"]["temp_min"],
                "max": item["main"]["temp_max"],
                "condition": item["weather"][0]["description"].title(),
                "icon": item["weather"][0]["icon"]
            })
            daily_dates.append(item["dt_txt"].split(" ")[0])
            daily_temps.append(item["main"]["temp"])

    # Generate chart
    plt.figure(figsize=(6, 4))
    plt.plot(daily_dates, daily_temps, marker="o", color="blue", linestyle="-")
    plt.title(f"5-Day Forecast for {current_weather['city']}")
    plt.xlabel("Date")
    plt.ylabel("Temp (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/forecast.png")
    plt.close()

    return current_weather, forecast_list


@app.route("/", methods=["GET", "POST"])
def index():
    city = "Chandigarh"  
    error = None
    weather = None
    forecast = None

    if request.method == "POST":
        city = request.form.get("city")

    weather, forecast = get_weather(city)

    if weather is None:
        error = f"Could not find weather data for '{city}'. Please try again."
        return render_template("index.html", error=error)

    return render_template("index.html", weather=weather, forecast=forecast)


if __name__ == "__main__":
    app.run(debug=True)
