# 2) Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.

import time

class Shop:

    total_sell = 0

    def __init__(self, name, sold):
        self.name = name
        self.sold = sold
        print('\n(Продажа в {0})'.format(self.name))
        Shop.total_sell += 1

    def Store_sold(self):
        print('Приветствую! Клиент совершил покупку в магазине {0}.'.format(self.name))
        time.sleep(0.4)

    def howMany():
        print('У нас {0:d} Продажи.'.format(Shop.total_sell))
        time.sleep(0.4)

    howMany = staticmethod(howMany)

obj1 = Shop('Auchan', 0)
obj1.Store_sold()
Shop.howMany()

obj2 = Shop('Silpo', 0)
obj2.Store_sold()
Shop.howMany()

print('\nВ', obj1.name, 'и', obj2.name, 'были продажи!'), Shop.howMany()