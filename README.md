# 🌱 Agro World v2.0 | Precision Agriculture Decision Support
Welcome to **Agro World v2.0**, a high-end digital ecosystem designed to empower farmers with laboratory-grade diagnostics and enterprise-level UI. We bridge the gap between traditional farming and modern software excellence, offering real-time intelligence, AI-driven crop pathology, and a seamless logistics marketplace.

---

## 🔥 What's New in v2.0
- **💎 Premium Software UI:** Completely overhauled interface featuring glassmorphism, dynamic background patterns, and a sleek high-tech aesthetic inspired by modern dev tool websites.
- **🧠 Neural Diagnostic Engine:** Enhanced AI disease detection terminal with low-latency cellular pattern analysis and simulated laboratory precision.
- **🇮🇳 Enhanced Bilingual Support:** Robust Telugu and Hindi integration with localized agricultural terminology (e.g., *బాక్టీరియా ఎండు తెగులు*) and bilingual labeling.
- **🌪️ Advanced Micro-animations:** Smooth transitions, rotating icons, and reactive terminal states for a superior "Wow" factor.

## 🚀 Core Features

- **🌤️ Weather Intelligence:** 5-day location-based forecasts with precision updates on rain, humidity, and frost alerts using Open-Meteo.
- **📰 Live Farming News:** Dynamic search-enabled agricultural news feeds utilizing live Google News RSS integration.
- **📈 Market Prices (Mandi):** Real-time Mandi market price tracking for the national APMC network.
- **💵 Government Schemes (Yojanas):** Intelligent directory for PM-Kisan, PMFBY, and KCC financial assistance programs.
- **🍃 Crop Intelligence:** Interactive optimization protocols for 30+ crops with comprehensive interactive skillsets.
- **📝 Smart Task Manager:** Data-driven activity tracker with dynamic counters and operation-specific reminders.
- **🚚 Logistics Marketplace:** Direct connect platform for manufacturers and transporters with context-aware AI chat support.

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
