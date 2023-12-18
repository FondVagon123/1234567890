from abc import ABC, abstractmethod

# Абстрактні класи для продуктів
class Wine(ABC):
    @abstractmethod
    def display(self):
        pass

class RedWine(Wine):
    def display(self):
        return "Red Wine"

class WhiteWine(Wine):
    def display(self):
        return "White Wine"

# Абстрактна фабрика
class WineFactory(ABC):
    @abstractmethod
    def create_wine(self) -> Wine:
        pass

# Конкретні фабрики
class RedWineFactory(WineFactory):
    def create_wine(self) -> Wine:
        return RedWine()

class WhiteWineFactory(WineFactory):
    def create_wine(self) -> Wine:
        return WhiteWine()

# Клас, який використовує абстрактну фабрику
class WineStore:
    def __init__(self, wine_factory: WineFactory):
        self.wine_factory = wine_factory

    def order_wine(self):
        wine = self.wine_factory.create_wine()
        print(f"Ordered: {wine.display()}")

# Приклад використання
red_wine_factory = RedWineFactory()
white_wine_factory = WhiteWineFactory()

store1 = WineStore(red_wine_factory)
store1.order_wine()

store2 = WineStore(white_wine_factory)
store2.order_wine()
