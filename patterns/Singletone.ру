# app.py
from flask import Flask, render_template
import copy

app = Flask(__name__)

class Wine:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

class WineCatalogSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(WineCatalogSingleton, cls).__new__(cls)
            cls._instance.catalog = []
        return cls._instance

    def add_wine(self, wine):
        self.catalog.append(wine)

    def get_catalog(self):
        return copy.deepcopy(self.catalog)

wine_catalog = WineCatalogSingleton()

# Початковий список вин
original_wines = [
    Wine("Merlot", 2018, 25.0),
    Wine("Chardonnay", 2019, 30.0),
    Wine("Cabernet Sauvignon", 2017, 40.0)
]

# Додаємо вина до каталогу
for wine in original_wines:
    wine_catalog.add_wine(wine)

@app.route('/')
def index():
    return render_template('index_singleton.html', wines=wine_catalog.get_catalog())

@app.route('/products')
def products():
    cloned_wines = [wine.clone() for wine in original_wines]
    return render_template('products.html', wines=cloned_wines)

if __name__ == '__main__':
    app.run(debug=True)
