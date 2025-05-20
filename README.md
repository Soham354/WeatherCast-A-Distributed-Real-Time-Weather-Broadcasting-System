# 🌦️ WeatherCast: A Distributed Real-Time Weather Broadcasting System

**WeatherCast** is a real-time chat application that integrates live weather updates using the [OpenWeather API](https://openweathermap.org/api). It demonstrates the principles of distributed computing by enabling multiple users to join secure chat rooms and receive real-time weather data shared by a designated broadcaster.

---

## 🚀 Features

- 🔐 Secure room access using randomly generated unique keys
- 🌍 Weather broadcasting by a single broadcaster per room via OpenWeather API
- 💬 Real-time messaging using WebSockets (Flask-SocketIO)
- 👥 Multi-user support per room with synchronized communication
- 📡 Automatic weather data sharing for users who cannot search manually
- 🖥️ Clean and responsive user interface
- ⚠️ Error handling for invalid city names or incorrect room keys

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask)  
- **Real-time Communication**: Flask-SocketIO  
- **API Integration**: OpenWeather API  
- **Deployment**: Localhost / Ready for cloud deployment (Heroku, AWS, etc.)

---

## 📁 Project Structure

WeatherCast/  
├── static/  
│ ├── css/  
│ └── js/  
├── templates/  
│ ├── index.html  
│ ├── chat.html  
│ └── weather.html  
├── app.py  
├── requirements.txt  
└── README.md

---

## ⚙️ Installation & Setup

1.**Clone the repository**
   ```bash
   git clone https://github.com/Soham354/WeatherCast-A-Distributed-Real-Time-Weather-Broadcasting-Systemt.git
   cd WeatherCast
   ```
2.**Create and activate a virtual environment**
   ```bash
   python -m venv venv
   For Windows: venv\Scripts\activate
   ```
3.**Install dependencies**   
   ```bash     
    pip install -r requirements.txt
   ```
4.**Set your OpenWeather API key**
 
    Open app.py
    Replace "YOUR_API_KEY" with your actual API key from OpenWeather
5.**Run the application**
   ```bash
   python app.py
   ```
6.**Open in browser**
   ```bash
   http://localhost:5000
   ```
**🧪 How It Works**
```bash
A user creates a room and becomes the broadcaster

A unique room key is generated and can be shared with others

Other users join as viewers

Broadcaster enters a city name → weather data is fetched and broadcast to the room

All users in the room can chat and view real-time weather updates
```
**🔮 Future Scope**
```   
Add user login/signup (authentication system)

Enable persistent chat history

Support for file sharing and multimedia messaging

Mobile-friendly design and layout

Role-based access control (broadcaster, viewer, moderator)

Live push notifications for weather alerts

Admin analytics dashboard
```


**🤝 Contributing**

Contributions are welcome!

Fork the repo, make changes, and submit a pull request. Let's build together!
