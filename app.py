#!/usr/bin/env python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""Learning REST API with Flask and Python."""

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [{
    'name': 'shoes',
    'items': [{
        'name': 'clark Shoes',
        'Price': 23.99
    }, {
        'name': 'caterpillar Shoe',
        'Price': 34.99
    }]
}, {
    'name': 'belts',
    'items': [{
        'name': 'dior Belt',
        'Price': 4.99
    }, {
        'name': 'gucci Belt',
        'Price': 2.99
    }]
}]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'item': []}
    stores.append(new_store)

    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_stores():
    """Returns a JSON object with main key and value as list of dictionaries."""
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['item'].append(new_item)
            return jsonify(new_item)

    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.run()
