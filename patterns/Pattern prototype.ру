# app.py
from flask import Flask, render_template
import copy

app = Flask(__name__)

class Wine:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

    def clone(self):
        return copy.deepcopy(self)

class PrototypeManager:
    def __init__(self):
        self.prototypes = {}

    def add_prototype(self, name, prototype):
        self.prototypes[name] = prototype

    def get_prototype(self, name):
        return self.prototypes.get(name)

prototype_manager = PrototypeManager()

# Початковий список вин
original_wines = [
    Wine("Merlot", 2018, 25.0),
    Wine("Chardonnay", 2019, 30.0),
    Wine("Cabernet Sauvignon", 2017, 40.0)
]

# Додайте вини до менеджера прототипів
for wine in original_wines:
    prototype_manager.add_prototype(wine.name, wine)

@app.route('/')
def index():
    return render_template('index.html', wines=original_wines)

@app.route('/products')
def products():
    cloned_wines = [wine.clone() for wine in original_wines]
    return render_template('products.html', wines=cloned_wines)

if __name__ == '__main__':
    app.run(debug=True)
