list = [15, 48, 'hello', 6, 19, 'world']
list2 = list[2] + list[5]
summa = 0
list.pop(2)
list.pop(4)
for i in list:
    if i%2==0:
        summa = summa + i // 10 + i % 10
    else:
        i = list.index(i)
        list[0] = 1
print(list)
print("Сумма четных чисел: ", summa)

gl = 0
sogl = 0
for x in list2:
    if x =="e" or x =="u" or x =="i" or x =="o" or x =="a":
        gl+=1
    else:
        sogl+=1
print("Глассные: ", gl, "Cогласные: ", sogl)
