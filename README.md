# 🌱 Agro World | Smart Farming Decision Support System

Welcome to **Agro World**, a comprehensive digital assistant designed to empower small-scale farmers with big-scale technology. Our platform bridges the gap between technology and traditional farming, offering real-time weather forecasts, crop disease guidance, and direct communication with suppliers.

---

## 🚀 Features

- **🌤️ Weather Intelligence:** Get 5-day location-based forecasts with precision updates on rain, humidity, and frost alerts. Keep track of hyperlocal weather conditions easily using Open-Meteo.
- **📰 Live Farming News:** Stay updated with the latest live agricultural and farming news to make informed market decisions. 
- **🍃 Crop Management & AI Disease Detection:** Identify diseases by uploading infected leaf photos, learn about organic fertilizers, and optimize sowing schedules for 30+ crops.
- **📝 Smart Task Manager:** Keep your activities structured with daily and weekly reminders for irrigation, fertilization, and pest control.
- **🚚 Direct Logistics Marketplace:** Connect directly with seed manufacturers and vehicle owners without any middlemen for better pricing and transparency.
- **🌍 Multi-Lingual Support:** Completely accessible in English, Hindi, and Telugu, empowering a wider range of farmers.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite
- **APIs:** Open-Meteo (Weather), Feedparser/BeautifulSoup4 (News Parsing), OpenStreetMap/Nominatim (Geocoding)

---

## 🖥️ Local Setup & Installation

Follow these steps to get a local copy up and running.

### 1. Clone the repository
```bash
git clone https://github.com/Bunnyvalluri/farming.git
cd farming/AgroWorldapp/backend
```

### 2. Create a virtual environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the `backend` directory (if not already present):
```env
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///agro_world.db
SECRET_KEY=your_secret_key_here
```

### 5. Run the application
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your web browser.

---

## ☁️ Deployment

The project is structured to deploy smoothly to serverless platforms such as **Vercel** or **Render**.
- **Read-Only Environments:** Handles `/tmp/` caching and database storage seamlessly for Vercel’s runtime. 
- Includes all standard production `requirements.txt`.

---

## 🤝 Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Empowering small-scale farmers with big-scale technology. © 2026 Agro World.*
