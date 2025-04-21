from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

TIMEZONES = {
    "Washington": "America/New_York",
    "Austin": "America/Chicago",          
    "Denver": "America/Denver", 
    "Sacramento": "America/Los_Angeles", 
    "Juneau": "America/Juneau", 
    "Honolulu": "Pacific/Honolulu",
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Tokyo": "Asia/Tokyo",
    "Canberra": "Australia/Sydney",
    "Seoul": "Asia/Seoul",
    "New Delhi": "Asia/Kolkata",
    "Brasilia": "America/Sao_Paulo"
}

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Token used is not authorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Missing city parameter"}), 400
    city = city.strip().title()
    tz = TIMEZONES.get(city)
    if not tz:
        return jsonify({"error": f"'{city}' is not in the database"}), 404

    now = datetime.now(pytz.timezone(tz))
    offset = now.strftime('%z')
    formatted_offset = f"UTC{'+' if int(offset) >= 0 else '-'}{offset[1:3]}:{offset[3:]}"
    return jsonify( {
        "city": city,
        "current_time": now.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": formatted_offset
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
