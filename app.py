import os
from openai import OpenAI
from flask import Flask, jsonify, request, send_from_directory, render_template  
from flask_cors import CORS
import json

LOGIN_DETAILS = {
    "email": "admin@gmail.com",
    "password": "Admin$887"
}

KEY = "YOUR_OPEN_AI_API_KEY"
client = OpenAI(
    api_key=KEY,
)
gpt_prompt = """Create a detailed travel plan for $DAY$-day, $STYLE$ trip to $CITY$, $STATE$. List activity time wise for days. Generate response only in below json format. json should be valid.
                format example: { "destination": "cityname and statename", "travel_plan": [{ "day": 1, "activities": [ { "time": "05:00AM", "activity": "visit", "location": "Japanese Garden", "description": "start your day with great visit to Japanese Garden" }, { "time": "06:00AM", "activity": "lunch", "location": "Hotel Maharaja", "description": "Sweet and great lunch" } ] }, { "day": 2, "activities": [ { "time": "04:00AM", "activity": "morning walk", "location": "JK streets", "description": "Good morning walk at jk streat" } ] } ] }"""

def build_promp(city, state, day, style):
    return gpt_prompt.replace("$CITY$", city).replace("$STATE$", state).replace("$DAY$", str(day)).replace("$STYLE$", style)

def chat_with_gpt(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo-0125",
    )
    
    return chat_completion.choices[0].message.content.strip();

def trip_plan(payload):
    prompt = build_promp(payload["city"],payload["state"],payload["day"],payload["travel_style"])
    gpt_response = chat_with_gpt(prompt)
    try:
        json_data = json.loads(gpt_response)
        return json_data
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return False


app = Flask(__name__, static_folder='dist')
cors = CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')




@app.route('/calculate', methods=['POST'])
def calculate():
    gpt_success = False;
    count = 0
    payload = json.loads(request.data)
    while(gpt_success == False and count < 3):
        gpt_success = trip_plan(payload)
        count+=1
        print("RE- Running the request")
    if(count >= 3):
        return jsonify({"error": True})
    return jsonify(gpt_success)

@app.route('/login', methods=['POST'])
def login():
    payload = json.loads(request.data)
    if (payload["email"] == LOGIN_DETAILS["email"] and payload["password"]==LOGIN_DETAILS["password"] ):
        return jsonify({"error": False, "message": "Successfull login"})
    return jsonify({"error": True, "message": "Unsuccessfull login, Try again!"})

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True, debug=True)