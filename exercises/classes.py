class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    @classmethod
    def class_method(cls):
        print(f'Creatng object of type {cls}')
        return cls(f'Own Store : {cls}')

    @staticmethod
    def static_method():
        print(f'Called static_method')

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + ' - franchise')

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return store.name + ', total stock price: ' + str(int(store.stock_price()))


storeBefore = Store.class_method()
store = Store('Lucky Buys')
store.add_item('pot', 12)
store.add_item('pan', 5)
store.add_item('screwdriver', 100)
Store.static_method()

print(storeBefore.name)
print(store.stock_price())
