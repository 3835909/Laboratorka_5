from restaurant import*
from User import*
from admin import Admin

vasya_petuhov = Admin('Вася', 'Петухов', 25, '+7922000002')
print(vasya_petuhov.first_name, vasya_petuhov.last_name, 'доступны следующие действия: ', ', '.join(vasya_petuhov.privileges.show_privileges()))

ivan_kobyakov = User('Иван', 'Кобяков', 30, '+79220000000')
sergey_ivanon = User('Сергей', 'Иванов', 18, '+79220000001')
ivan_kobyakov.increment_login_attempts()
ivan_kobyakov.increment_login_attempts()
print(f'Выводим счётчик login_attemps {ivan_kobyakov.login_attempts}')
ivan_kobyakov.reset_login_attempts()
print(f'Обнуляем счётчик login_attempts, теперь он равен - {ivan_kobyakov.login_attempts}')
ivan_kobyakov.describe_user()
ivan_kobyakov.greet_user()
sergey_ivanon.describe_user()
sergey_ivanon.greet_user()
restoran_china = Restaurant('Шангри-Ла', 'Китайская кухня')
restoran_japan = Restaurant('Якитория', 'Японская кухня')
restoran_uzbek = Restaurant('Нигора', 'Узбекская кухня')
restoran_china.increment_number_served(5)
print(f'Количество посетителей в {restoran_china.restaurant_name} : {restoran_china.count_visitor} человек')
restoran_china.describe_restaurant()
restoran_japan.describe_restaurant()
restoran_uzbek.describe_restaurant()
kiosk_ice_cream = IceCreamStand('Мини киоск', 'Шоколадное мороженое', ['пломбир', 'эскимо'])
kiosk_ice_cream.list_flavors()

