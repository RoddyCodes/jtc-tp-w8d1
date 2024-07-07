from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

key = '21db1d4d9e7543e598010800240207'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'



@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    url = f"{BASE_URL}?key={key}&q={city}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City is not found"}), 404

    data = response.json()
    weather_info = {
        "city": data['location']['name'],
        "temperature": data['current']['temp_c'],
        "condition": data['current']['condition']['text'],
        "humidity": data['current']['humidity'],
        "wind_speed": data['current']['wind_kph']
    }
    
    return jsonify(weather_info), 200

if __name__ == '__main__':
    app.run(debug=True)
