# Weather Forecast Web App

A simple weather forecasting web app built with **Flask** + **OpenWeatherMap API** + **Matplotlib**.  
It shows **current weather**, a **5-day forecast**, and a **temperature trend chart**.  
Deployed on [Vercel](https://weather-forecasting-psi-one.vercel.app/) ✅

---

## Features
- Search weather by city name  
- Real-time current weather data (temperature, humidity, wind, condition, icon)  
- 5-Day forecast (min/max temp + weather icons)  
- Temperature trend line chart generated with Matplotlib  
- Responsive, modern UI with TailwindCSS  
- Deployed serverlessly on Vercel (Python runtime)  

---

## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML (Jinja2), TailwindCSS  
- **APIs:** [OpenWeatherMap](https://openweathermap.org/api)  
- **Charts:** Matplotlib (rendered as Base64 images in HTML)  
- **Deployment:** Vercel  

---

## Project Structure
```

├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── vercel.json
└── README.md

````

---

## ⚙️ Setup (Local Development)

1. **Clone the repo**
```bash
git clone https://github.com/Anonymous120324/Weather-forecasting.git
cd Weather-forecasting
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Get your OpenWeatherMap API Key**

   * Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   * Create a `.env` file in the project root:

```bash
API_KEY=your_api_key_here
```

4. **Run locally**

```bash
flask run
```

Open 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000) 
