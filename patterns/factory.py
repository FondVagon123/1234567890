# Абстрактний клас для продукту
class Wine(ABC):
    @abstractmethod
    def display(self):
        pass
 
# Конкретний клас продукту
class RedWine(Wine):
    def display(self):
        return "Це червоне вино"
 
# Інший конкретний клас продукту
class WhiteWine(Wine):
    def display(self):
        return "Це біле вино"
 
# Абстрактна фабрика
class WineFactory(ABC):
    @abstractmethod
    def create_wine(self):
        pass
 
# Конкретна фабрика для червоного вина
class RedWineFactory(WineFactory):
    def create_wine(self):
        return RedWine()
 
# Конкретна фабрика для білого вина
class WhiteWineFactory(WineFactory):
    def create_wine(self):
        return WhiteWine()
 
# Клас клієнта, який використовує фабрику для створення продукту
class WineStore:
    def init(self, wine_factory):
        self.wine_factory = wine_factory
 
    def order_wine(self):
        wine = self.wine_factory.create_wine()
        return wine.display()
 
# Використання
if name == "main":
    # Використовуємо фабрику для створення червоного вина
    red_wine_factory = RedWineFactory()
    red_wine_store = WineStore(red_wine_factory)
    red_wine = red_wine_store.order_wine()
    print(red_wine)  # Виведе "Це червоне вино"
 
    # Використовуємо фабрику для створення білого вина
    white_wine_factory = WhiteWineFactory()
    white_wine_store = WineStore(white_wine_factory)
    white_wine = white_wine_store.order_wine()
    print(white_wine)  # Виведе "Це біле вино"
