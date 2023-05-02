import time

print("Tere! Olen sinu uus sõber - Python!")
time.sleep(0.500) # Задержка отображения строки в 0,5 секунды.
nimi = input("Sissesta oma nimi: ")

print()
print(f"{nimi}, oi kui ilus nimi!")
time.sleep(1)
print()
answer = input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
print()


if answer == '1':
    while (True):
        
        try:
            pikkus = int(input("Sissesta enda pikkus: ")) # 1. Присваивание переменной pikkus целого значения переменной введенной пользователем. int()
            if 145 <= pikkus < 270:
                break
            elif pikkus < 150:
                print("Sa ei või olla nii lühike. Proovi sissestada õige pikkus.")
            elif pikkus >= 270:
                print("Sa ei saa olla nii pikk.")
        except:
            ValueError
            print("Sa sissestasid vale pikkus!")

    while (True):
        try:
            mass = float(input("Sissesta enda mass: ")) # 2. Присваивание переменной mass значения выражения в формате действительного числа. float()
            if 30 <= mass < 400:
                break
            elif mass < 30 or mass > 400:
                print("Sa vist kirjutasid vale massi number.")
        except:
            ValueError
            print("Sa sissestasid midagi tekst, aga mitte mass.")
    
    indeks = mass/pow((0.01*pikkus),2) # 3. Присваивание переменной indeks значения выражения mass /(0.01pikkus)2

    print()
    time.sleep(1)
    print(f"{nimi}! Sinu keha index: {round(indeks,1)}") # 4. Вывод на экран имени, объединённого с текстом "! Sinu keha indeks on:" indeks с одним знаком после запятой. round()

    # 5. Вывод оценки индекса массы тела в соответствии с таблицей:
    if indeks < 16:
        print("Tervisele ohtlik alakaal")
    elif 16 <= indeks < 19:
        print("Alakaal")
    elif 19 <= indeks < 25:
        print("Normaalkaal")
    elif 25 <= indeks < 30:
        print("Ülekaal")
    elif 30 <= indeks < 35:
        print("Rasvumine")
    elif 35 <= indeks <= 40:
        print("Tugev rasvumine")
    elif indeks > 40:
        print("Tervisele ohtlik rasvumine")


elif answer == '0':
    print("Kahju! See on väga kasulik info!") # 1.Вывод на экран текста "Kahju! See on väga kasulik info!"
    print() # 2. Вывод на экран пустой строки

else:
    print("Sa sissestasid vale valik.")

print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
    



