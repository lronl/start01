#1
lis = [i for i in range(50)]
num = 1
out = [] 
while(num < len(lis)): 
	if lis[num] % 2 == 0: 
		out.append(lis[num]) 
	num += 1
print(out) 

#2
Capitals = dict()
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'
Countries = ['Russia', 'France', 'USA', 'Russia']
for country in Countries:
    if country in Capitals:
        print('Столица страны ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)

#3
for x in range(1, 100):
    s = '';
    if x % 3 == 0:
        s += 'Fizz'
    if x % 5 == 0:
        s += "Buzz"
    if s == '':
        s = x
    print(s, end=' ')
	
#4
amount = input("Сумма депозита: ")
amount = int(amount)
pct = input("Процент: ")
pct = int(pct)
years = input("кол-во лет: ")
years = float(years)
 
pct = pct / 100 
month_pay = (amount * pct * (1 + pct)**years) / (12 * ((1 + pct)**years - 1))
print("Ваш месячный платеж составит: %.2f" % month_pay)
 
summa = month_pay * years * 12
print("За весь период вы заплатите: %.2f" % summa)
print("Это составит %.2f%% от первоначальной суммы" % ((summa / amount) * 100))
