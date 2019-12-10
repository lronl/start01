import time
class Shop:
    quantity: int
    store = 'shop'

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        print("Store ready")

my_shop = Shop('Auchan', 2)
my_sold = Shop(1, 0)

i = 0
while i < 10:
    print('Auchan Sell:', i, 'Goods')
    i = i + 1
    time.sleep(0.4)

print(my_shop.name, 'Total Sell :', my_sold.quantity + i)
