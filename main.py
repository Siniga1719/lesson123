password = 1111
summa_na_schete = 150
while True:
    passq = int(input("Для того, чтобы продолжить, Введите пароль: "))
    if passq == password:
        print("Пароль введен верно!")
        choose = int(input("Выберите действие: \n 1) Вывести остаток на карте. \n 2) Снять деньги. \n Введите номер действия: "))
        if choose == 1:
            print(summa_na_schete)
        elif choose == 2:
            print("Остаток на счете: ", summa_na_schete)
            snyatie = int(input("Какую сумму желаете снять? \n Введите сумму: "))
            if 0<snyatie<summa_na_schete:
                summa_na_schete = summa_na_schete - snyatie
                print("Вы сняли: ", snyatie, ".", "Ваш остаток: ", summa_na_schete)
            else:
                print("Вы ввели неверную сумму, попробуйте еще раз.")
                continue
        else:
            print('Неверный выбор, попробуйте еще раз.')
            continue
    else:
        print("Вы ввели неверный пароль, попробуйте еще раз.")
        continue
