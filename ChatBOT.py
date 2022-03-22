import random
import json
from flask import Flask, request, json, jsonify
import time
app = Flask(__name__)
from chatgui import chatbot_response

@app.route("/", methods=["POST", "GET"])
def response():
    if request.method == "GET":
        return "welcome..!!"

    elif request.method == "POST":
        query = dict(request.form)['query']
        print(query)
        res = chatbot_response(query)
        '''if query in ["Hi there", "How are you", "Is anyone there?", "Hey", "Hola", "Hello", "Good day", "hi", "hy", "hello"]:
            res = random.choice(["Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?"])
        if query in ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"]:
            res = random.choice(["See you!", "Have a nice day", "Bye! Come back again soon."])
        if query in ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"]:
            res = random.choice(["Happy to help!", "Any time!", "My pleasure"])
        if query in []:
            res = random.choice(["Sorry, can't understand you","Please give me more info", "Not sure I understand"])'''
        print(res)
        return jsonify({"response": res})

    else:
        return "Not Found..!!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
