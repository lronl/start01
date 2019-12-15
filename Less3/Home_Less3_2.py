# 2) Создать класс структуры данных Стек, Очередь.

import queue
import threading
import time

def putting_thread(q):
    while True:
        print('Start: ')
        time.sleep(10)
        q.put(5)
        print('end: ')

q = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q,))
t.start()

q.put(0)
print(q.get(), 'First Item')
print('------')

print(q.get(), ' Finish')







