from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv
import os
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_dir = '/tmp/.cache' if os.environ.get("VERCEL") == "1" else '.cache'
cache_session = requests_cache.CachedSession(cache_dir, expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "agro_world_super_secret_key")

db_url = os.getenv("DATABASE_URL")
if not db_url:
    db_url = "sqlite:////tmp/agro_world.db" if os.environ.get("VERCEL") == "1" else "sqlite:///agro_world.db"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

# Models
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    category = db.Column(db.String(50))
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create tables
with app.app_context():
    db.create_all()

MOCK_CROP_CARE = [
    {
        "name_key": "wheat_name",
        "diseases_keys": ["wheat_d1", "wheat_d2"],
        "care_key": "wheat_care",
        "icon": "fa-wheat-awn"
    },
    {
        "name_key": "rice_name",
        "diseases_keys": ["rice_d1", "rice_d2"],
        "care_key": "rice_care",
        "icon": "fa-seedling"
    },
    {
        "name_key": "cotton_name",
        "diseases_keys": ["cotton_d1", "cotton_d2"],
        "care_key": "cotton_care",
        "icon": "fa-cloud"
    },
    {
        "name_key": "soya_name",
        "diseases_keys": ["soya_d1", "soya_d2"],
        "care_key": "soya_care",
        "icon": "fa-leaf"
    },
    {
        "name_key": "corn_name",
        "diseases_keys": ["corn_d1", "corn_d2"],
        "care_key": "corn_care",
        "icon": "fa-sun" # Using fa-sun/seedling as substitute
    },
    {
        "name_key": "cane_name",
        "diseases_keys": ["cane_d1", "cane_d2"],
        "care_key": "cane_care",
        "icon": "fa-cubes-stacked"
    },
    {
        "name_key": "sun_name",
        "diseases_keys": ["sun_d1", "sun_d2"],
        "care_key": "sun_care",
        "icon": "fa-sun"
    }
]

import requests

def get_live_weather(lat=21.1458, lon=79.0882, custom_city=None):
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
            "daily": ["weather_code", "temperature_2m_max", "precipitation_sum"],
            "timezone": "auto"
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        
        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()
        current_relative_humidity_2m = current.Variables(1).Value()
        current_weather_code = current.Variables(2).Value()
        current_wind_speed_10m = current.Variables(3).Value()

        daily = response.Daily()
        daily_weather_code = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
        daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()
        
        # Reverse Geocoding to get actual city
        city_name = custom_city or "Your Location"
        if not custom_city:
            try:
                import requests as req
                geo_res = req.get(f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json", headers={'User-Agent': 'AgroWorldApp/1.0'}, timeout=2)
                if geo_res.status_code == 200:
                    addr = geo_res.json().get('address', {})
                    city_name = addr.get('city', addr.get('town', addr.get('village', addr.get('county', 'Unknown Location'))))
            except Exception:
                pass
        
        # Weather code mapping (simplified)
        codes = {0: "Sunny", 1: "Mainly Clear", 2: "Partly Cloudy", 3: "Overcast", 45: "Foggy", 51: "Drizzle", 61: "Rainy", 71: "Snowy", 80: "Rain Showers", 95: "Thunderstorm"}
        
        # Calculate Mock Alerts
        alerts = []
        if current_wind_speed_10m > 20:
            alerts.append({"type": "warning", "text": f"⚠️ Wind Speed Alert: > {int(current_wind_speed_10m)}km/h"})
            
        precipitation_sum_today = daily_precipitation_sum[0]
        if precipitation_sum_today > 10:
            alerts.append({"type": "danger", "text": "🚨 Heavy Rainfall Prediction (Next 24h)"})

        smart_tip = None
        if precipitation_sum_today > 10:
            smart_tip = "“Avoid fertilizer & pesticide spraying in the next 24 hours due to predicted heavy rains.”"
        elif current_wind_speed_10m > 20:
             smart_tip = "“Avoid spraying pesticides today due to high wind speeds.”"
        
        weather_data = {
            "current": {
                "temp": round(current_temperature_2m, 1),
                "condition": codes.get(int(current_weather_code), "Clear"),
                "humidity": round(current_relative_humidity_2m),
                "wind": round(current_wind_speed_10m, 1),
                "location": f"{city_name} (Live)"
            },
            "alerts": alerts,
            "smart_tip": smart_tip,
            "forecast": []
        }
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        today_idx = datetime.now().weekday()
        
        for i in range(5):
            day_idx = (today_idx + i) % 7
            weather_data["forecast"].append({
                "day": days[day_idx],
                "temp": f"{daily_temperature_2m_max[i]:.1f}",
                "cond": codes.get(int(daily_weather_code[i]), "Sunny")
            })
        return weather_data
    except Exception as e:
        print(f"Weather Error: {e}")
        return None

def get_live_news(query="agriculture OR farming india"):
    try:
        import feedparser
        import urllib.parse
        from bs4 import BeautifulSoup
        
        safe_query = urllib.parse.quote(query)
        # Using Google News RSS with requests for timeout control
        url = f"https://news.google.com/rss/search?q={safe_query}&hl=en-IN&gl=IN&ceid=IN:en"
        import requests
        response = requests.get(url, timeout=5)
        feed = feedparser.parse(response.content)
        
        images = [
            "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&w=400",
            "https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?auto=format&fit=crop&w=400",
            "https://images.unsplash.com/photo-1560493676-04071c5f467b?auto=format&fit=crop&w=400",
            "https://images.unsplash.com/photo-1495107334309-fcf20504a5ab?auto=format&fit=crop&w=400",
            "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&w=400"
        ]
        
        news_items = []
        for i, entry in enumerate(feed.entries[:6]): # Get top 6 live news
            soup = BeautifulSoup(entry.summary, "html.parser")
            desc = soup.get_text()[:150] + "..." if soup.get_text() else "Read more about this agricultural update..."
            # Bing provides source publisher in entry.source if available, else extract from title
            publisher = "Agriculture News"
            if hasattr(entry, 'source') and hasattr(entry.source, 'title'):
                publisher = entry.source.title
            title = entry.title
            
            # Simple timezone parse mapping
            import email.utils
            from datetime import timezone
            
            try:
                dt = email.utils.parsedate_to_datetime(entry.published)
                diff = datetime.now(timezone.utc) - dt
                if diff.days > 0:
                    time_str = f"{diff.days} days ago"
                elif diff.seconds > 3600:
                    time_str = f"{diff.seconds // 3600} hours ago"
                else:
                    time_str = f"{diff.seconds // 60} minutes ago"
            except Exception:
                time_str = "Recently"

            news_items.append({
                "title": title,
                "desc": desc,
                "publisher": publisher,
                "category": "Live Updates",
                "time": time_str,
                "img": images[i % len(images)],
                "link": entry.link
            })
            
        if not news_items:
            # Fallback mock data in case RSS fails, is blocked, or returns empty
            news_items = [
                {
                    "title": f"Government announces new subsidies for {query.replace('OR farming india', '').strip() or 'Agriculture'} farmers",
                    "desc": "The Ministry of Agriculture has outlined a new set of comprehensive financial subsidies aimed at boosting technology adoption in rural farming subsectors...",
                    "publisher": "Agri Business News",
                    "category": "Policy",
                    "time": "2 hours ago",
                    "img": images[0],
                    "link": "https://krishijagran.com/news/" # Real matter link
                },
                {
                    "title": f"New hybrid seed variants of {query.replace('OR farming india', '').strip() or 'Wheat'} yield 20% more output",
                    "desc": "Agricultural research institutes have successfully completed trials on a new strain that is both drought-resistant and significantly more productive...",
                    "publisher": "Science Daily",
                    "category": "Innovation",
                    "time": "5 hours ago",
                    "img": images[1],
                    "link": "https://www.scidev.net/asia-pacific/agriculture/" # Real matter link
                },
                {
                    "title": "Monsoon forecast looks promising for the upcoming Kharif season",
                    "desc": "Meteorologists predict a normal to above-normal monsoon this year, bringing relief to millions of farmers relying on rain-fed agriculture...",
                    "publisher": "Weather Today",
                    "category": "Live Updates",
                    "time": "12 hours ago",
                    "img": images[2],
                    "link": "https://pib.gov.in/indexd.aspx" # Real matter link
                }
            ]
        
        return news_items
    except Exception as e:
        print(f"News Error: {e}")
        return [
            {
                "title": "Unable to fetch live news at the moment due to network issues",
                "desc": "Please check your internet connection or try searching again later. The server might be rate-limited by the news provider.",
                "publisher": "System Alert",
                "category": "System Alert",
                "time": "Just now",
                "img": "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&w=400",
                "link": "https://krishijagran.com/" # Real matter fallback
            }
        ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    lat = request.args.get('lat', default=21.1458, type=float)
    lon = request.args.get('lon', default=79.0882, type=float)
    city_param = request.args.get('city')
    
    custom_city = None
    if city_param:
        try:
            import requests as req
            geo_res = req.get(f"https://nominatim.openstreetmap.org/search?q={city_param}&format=json&limit=1", headers={'User-Agent': 'AgroWorldApp/1.0'}, timeout=2)
            if geo_res.status_code == 200 and len(geo_res.json()) > 0:
                lat = float(geo_res.json()[0]['lat'])
                lon = float(geo_res.json()[0]['lon'])
                custom_city = geo_res.json()[0].get('name', city_param).title()
        except:
            pass

    live_data = get_live_weather(lat, lon, custom_city)
    if not live_data:
        # Simplified fallback
        live_data = {"current": {"temp": 28, "condition": "Sunny", "location": "Nagpur (Offline)"}, "forecast": []}
    return render_template('weather.html', weather=live_data)

@app.route('/news')
def news():
    query = request.args.get('q', 'agriculture OR farming india')
    news_items = get_live_news(query)
    return render_template('news.html', news=news_items, query=query)

@app.route('/tasks')
def tasks_view():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        category=data.get('category', 'General')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"success": True, "id": new_task.id})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"success": True})

@app.route('/api/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.is_completed = not task.is_completed
    db.session.commit()
    return jsonify({"success": True, "status": task.is_completed})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simple session logic for "Real World" feel
        session['user_id'] = 1
        session['user_name'] = "Rahul"
        return redirect(url_for('index'))
    return render_template('auth.html', type='login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template('auth.html', type='register')

@app.route('/crop-care')
def crop_care():
    return render_template('crop_care.html', crops=MOCK_CROP_CARE)

@app.route('/logistics')
def logistics():
    return render_template('logistics.html')

@app.route('/schemes')
def schemes():
    return render_template('schemes.html')

@app.route('/market')
def market():
    return render_template('market.html', page_title='Market Price Index')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
