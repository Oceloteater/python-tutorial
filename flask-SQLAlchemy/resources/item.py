import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field is required')

    @jwt_required()  # auth on call
    def get(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.get_by_name(name):
            return {'message': 'An item of "{}" already exists'.format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted from db'}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = 'DELETE FROM items WHERE name=?'
        # cursor.execute(query, (name,))
        #
        # connection.commit()
        # connection.close()
        #
        # return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.get_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            item = ItemModel(name, data['price'])
            # try:
            #     updated_item.save_to_db()
            # except:
            #     return {'message': 'An error occurred inserting the item'}, 500
        else:
            item.price = data['price']
            # try:
            #     updated_item.update()
            # except:
            #     return {'message': 'An error occurred updating the item'}, 500
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items'
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}
