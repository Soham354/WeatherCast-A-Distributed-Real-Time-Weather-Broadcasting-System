from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, send, join_room, disconnect, ConnectionRefusedError
import requests, random, string

app = Flask(__name__)
app.secret_key = "super-secret-key"
socketio = SocketIO(app, cors_allowed_origins="*")

API_KEY = "6b8362a3950ef5031cbbee10511fa4df"
ROOM_KEY = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
ROOM = "weather_chat"

broadcaster_sid = None  # Store socket ID of broadcaster


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def weather():
    
    if session.get("is_owner"):
        return render_template("weather.html")
    return redirect(url_for("chat"))


@app.route("/chat", methods=["GET", "POST"])
def chat():
    global broadcaster_sid

    
    if session.get("is_owner") and session.get("joined"):
        return render_template("chat.html", room_key=ROOM_KEY, is_owner=True)

    if request.method == "POST":
        entered_key = request.form.get("room_key")
        if entered_key == ROOM_KEY:
            session["joined"] = True

           
            if broadcaster_sid is None:
                session["is_owner"] = True
            else:
                session["is_owner"] = False

            return render_template("chat.html", room_key=ROOM_KEY, is_owner=session["is_owner"])
        else:
            return render_template("join.html", error="❌ Invalid key. Try again.")

    return render_template("join.html", error=None)


@app.route("/get_weather", methods=["POST"])
def get_weather():
    if not session.get("is_owner"):
        return {"error": "Only the broadcaster can send weather updates."}, 403

    city = request.form["city"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return {"error": "City not found"}, 404

    description = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    message = f"📡 Weather Update - {city}: {description}, {temp}°C"

    socketio.emit("message", message, room=ROOM)
    return {"message": message}, 200


@socketio.on("connect")
def handle_connect():
    global broadcaster_sid

    if not session.get("joined"):
        raise ConnectionRefusedError("Not allowed")

    
    join_room(ROOM)

  
    if session.get("is_owner") and broadcaster_sid is None:
        broadcaster_sid = request.sid
    elif session.get("is_owner") and broadcaster_sid != request.sid:
        
        session["is_owner"] = False
        send("❌ Duplicate broadcaster rejected.", room=request.sid)
        return

   
    if not session.get("is_owner"):
        send("👋 A new user has joined the chat!", room=ROOM)


@socketio.on("disconnect")
def handle_disconnect():
    global broadcaster_sid

    if session.get("is_owner") and request.sid == broadcaster_sid:
       
        broadcaster_sid = None
        session["is_owner"] = False
        print("🔌 Broadcaster disconnected.")
    elif session.get("joined"):
        send("❌ A user has left the chat.", room=ROOM)


@socketio.on("message")
def handle_message(msg):
    send(msg, room=ROOM)


if __name__ == "__main__":
    print(f"🔑 Room Key (Owner Key): {ROOM_KEY}")
    socketio.run(app, debug=True)
