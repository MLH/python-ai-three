from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import config
from markov_bot import generate_bot_answer
from content_moderator import moderate

app = Flask(__name__)
socketio = SocketIO(app)


# Renders UI
@app.route("/")
def home():
    return render_template("homepage.html")


# Chat API - WebSocket
@socketio.on("send question")
def generate_message(body, methods=["POST"]):
    question = body["message"]
    twitter_handle = body["username"]

    try:
        bot_answer = generate_bot_answer(twitter_handle, question)
        if bot_answer == None:
          answer = {"username": twitter_handle, "message": bot_answer}
        else:
          moderated_bot_answer = moderate(bot_answer)
          answer = {"username": twitter_handle, "message": moderated_bot_answer}
        socketio.emit("bot answer", answer)
    except:
        bot_answer = "Sorry, I couldn't process that. Try again please."
        error_message = {"username": twitter_handle, "message": bot_answer}
        socketio.emit("error", error_message)

        
if __name__ == "__main__":
    socketio.run(app)

