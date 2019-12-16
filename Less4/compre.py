import time

start = time.time()
a = []
for i in range(100):
    if i % 2 == 0:
        a.append(i)
print(a)
end = time.time() - start


dict = {
    1: 2,
    3: 4,
    5: 6
}
start_compr = time.time()
odds = [(i, i) for i in range(100) if i % 2 == 0]
print(odds)
odds1 = {(i, j) for i, j in dict.items()}
print(odds1)
end_compr = time.time() - start_compr

if end_compr < end:
    print('Compr are faster')
