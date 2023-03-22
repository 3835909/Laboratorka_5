class Restaurant():
    """Создание класса Ресторан"""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты класса ресторан"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.count_visitor = 0

    def describe_restaurant(self):
        """Выводит 2 атрибута класса ресторан"""
        print(self.restaurant_name + ' ' + self.cuisine_type)

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт"""
        print('Ресторан открыт')

    def increment_number_served(self, visitor):
        """Увеличивает количество обслуженных клиентов"""
        self.count_visitor += visitor


class IceCreamStand(Restaurant):
    """Создание класса IceCreamStand наследующего от класса Restaurant"""
    flavors = []
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Инициализация класса"""
        super().__init__(restaurant_name, cuisine_type)
        """Наследование от родительского класса Restaurant"""
        self.flavors = flavors

    def list_flavors(self):
        """Вывод списка flavors"""
        print(', '.join(self.flavors))