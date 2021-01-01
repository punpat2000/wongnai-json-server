# for local json server please run command python app.py

from flask import request, Flask, jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

with open('db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
        
@app.route('/', methods=['GET'])
def index():
    return 'it works! Pattradanai Punvichartkul'

@app.route('/trips')
def trips():
    return jsonify(data)

@app.route('/api/trips')
def trip_query():
    header = request.args.get('keywords', type = str)
    if header == '':
        return trips()
    trip_list = data['trips']
    matched_items = list()
    for trip in trip_list:
        if header in trip['title']:
            matched_items.append(trip)
            continue
        if header in trip['description']:
            matched_items.append(trip)
            continue
        if header in trip['tags']:
            matched_items.append(trip)
            continue
    return jsonify(trips = matched_items)

# if __name__ == '__main__':
#   app.debug = True
#   app.run(host='0.0.0.0', port=8000)