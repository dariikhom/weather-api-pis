from flask import Flask, render_template_string
import requests

app = Flask(__name__)

API_KEY = '77340edf46cccf44481514632c338b3a'
CITY = 'Kyiv'
UNITS = 'metric'

@app.route('/')
def weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}&lang=uk'
    response = requests.get(url)
    data = response.json()
    
    if data.get('cod') != 200:
        return f"Помилка: {data.get('message')}"
    
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    
    html = f"""
    <h1>Погода у місті {CITY}</h1>
    <p>Температура: {temp}°C</p>
    <p>Опис: {description}</p>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
