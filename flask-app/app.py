from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])  # POST /store data: { name: string }
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')  # GET /store/<string:name>
def get_store(name):
    # iterate over stores
    for store in stores:
        if store['name'] == name:
            return jsonify({'store': store})
    return jsonify({'message': 'Error - store not found'})


@app.route('/store')  # GET /store
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Error - store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    # iterate over stores
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Error - store not found'})


app.run(port=5000)