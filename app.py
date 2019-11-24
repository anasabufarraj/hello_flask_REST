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
    """Returns home page template.
    
    :return: rendered template
    """
    return render_template('index.html')


@app.route('/store', methods=['POST'])
def create_store():
    """Creates a new store and returns it as jsonify object.
    
    :return: jsonify new created 'store' object.
    """
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)

    return jsonify(new_store)


@app.route('/store/<string:store_name>')
def get_store(store_name):
    """Returns a store name if exists, otherwise returns jsonified 'not found' object.
    
    :param store_name: string
    :returns: jsonify 'store' object, or jsonified 'not found' object.
    """
    for store in stores:
        if store['name'] == store_name:
            return jsonify(store)

    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_all_stores():
    """Returns a JSON object contains all stores with main key and a value as list of dictionaries.
    
    :return: jsonify 'stores' object.
    """
    return jsonify({'stores': stores})


@app.route('/store/<string:store_name>/item', methods=['POST'])
def create_item_in_store(store_name):
    """ TODO: add description
    
    :param store_name: string
    :return: jsonify 'store' object, or jsonified 'not found' object.
    """
    request_data = request.get_json()
    for store in stores:
        if store['name'] == store_name:
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'message': 'store not found'})


@app.route('/store/<string:store_name>/items')
def get_items_in_store(store_name):
    """Returns store items if exist, otherwise returns a jsonify 'not found' object.
    
    :param store_name: string
    :returns: jsonify 'store' object, or jsonified 'not found' object.
    """
    for store in stores:
        if store['name'] == store_name:
            return jsonify({'items': store['items']})

    return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.run()
