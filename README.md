# 🌱 Agro World | Smart Farming Decision Support System

Welcome to **Agro World**, a comprehensive digital assistant designed to empower small-scale farmers with big-scale technology. Our platform bridges the gap between technology and traditional farming, offering real-time weather forecasts, crop disease guidance, and direct communication with suppliers.

---

## 🚀 Features

- **🌤️ Weather Intelligence:** Get 5-day location-based forecasts with precision updates on rain, humidity, and frost alerts. Keep track of hyperlocal weather conditions easily using Open-Meteo.
- **📰 Live Farming News & Search:** Stay updated with the latest live agricultural news. Features a dynamic search engine allowing farmers to directly search for live updates on any specific crop, policy, or weather event (with real publisher sourcing).
- **📈 Market Prices (Mandi):** View real-time Mandi market prices to track price trends of crops like Wheat, Rice, and Cotton across multiple states.
- **💵 Government Schemes (Yojanas):** Discover and apply for financial assistance schemes, including PM-Kisan, PMFBY (Crop Insurance), KCC, and more.
- **🍃 Premium Crop Management:** Explore highly detailed, crop-specific best practices for Wheat, Rice, Cotton, Soybean, Corn, Sugarcane, and Sunflower. Includes an AI Disease Detection simulation.
- **📝 Glassmorphism Task Manager:** Keep your activities structured with a completely redesigned, dynamic daily/weekly planner featuring live progress tracking for irrigation, fertilization, and pest control.
- **🚚 Smart Logistics Support:** Connect directly with seed manufacturers and vehicle owners. Includes a smart keyword-based Chatbot assistant to quickly resolve booking, capacity, and pricing queries.
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
