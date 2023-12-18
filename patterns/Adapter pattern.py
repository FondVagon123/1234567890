from flask import Flask, render_template
import copy

app = Flask(__name__)

class Wine:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

class WineService:
    def get_wine_list(self):
        pass

    def get_wine_details(self, wine_id):
        pass

class WineShopUI:
    def show_wine_list(self):
        pass

    def show_wine_details(self, wine_id):
        pass

class WineShopAdapter(WineShopUI):
    def __init__(self, wine_service):
        self.wine_service = wine_service

    def show_wine_list(self):
        return self.wine_service.get_wine_list()

    def show_wine_details(self, wine_id):
        return self.wine_service.get_wine_details(wine_id)

class WineServiceImpl(WineService):
    def __init__(self):
        self.catalog = []

    def add_wine(self, wine):
        self.catalog.append(wine)

    def get_wine_list(self):
        return copy.deepcopy(self.catalog)

    def get_wine_details(self, wine_id):
        for wine in self.catalog:
            if wine.name == wine_id:
                return wine

wine_service_impl = WineServiceImpl()
wine_shop_adapter = WineShopAdapter(wine_service_impl)

# Початковий список вин
original_wines = [
    Wine("Merlot", 2018, 25.0),
    Wine("Chardonnay", 2019, 30.0),
    Wine("Cabernet Sauvignon", 2017, 40.0)
]

# Додаємо вина до каталогу
for wine in original_wines:
    wine_service_impl.add_wine(wine)

@app.route('/')
def index():
    wines = wine_shop_adapter.show_wine_list()
    return render_template('index_adapter.html', wines=wines)

@app.route('/products/<wine_id>')
def product_details(wine_id):
    wine_details = wine_shop_adapter.show_wine_details(wine_id)
    return render_template('product_details_adapter.html', wine=wine_details)

if __name__ == '__main__':
    app.run(debug=True)
