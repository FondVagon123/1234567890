class Wine:
    def __init__(self, name, year, price, country):
        self.name = name
        self.year = year
        self.price = price
        self.country = country

class WineBuilder:
    def __init__(self, name):
        self.wine = Wine(name, None, None, None)

    def set_year(self, year):
        self.wine.year = year
        return self

    def set_price(self, price):
        self.wine.price = price
        return self

    def set_country(self, country):
        self.wine.country = country
        return self

    def build(self):
        return self.wine

# Використання Builder для створення об'єкта вина
builder = WineBuilder("Merlot")
merlot_2015 = builder.set_year(2015).set_price(25.99).set_country("Italy").build()

# Виведення інформації про вино
print(f"{merlot_2015.name} ({merlot_2015.year}) - {merlot_2015.country} - ${merlot_2015.price:.2f}")
