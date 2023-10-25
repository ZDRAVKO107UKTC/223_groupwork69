opashka = [] #Празен лист

while True: #безкраен цикъл
    klienti = input()#пРОМЕНЛИВА КОЯТО ПРИЕМА ТЕКСТ
    
    if klienti == "END".lower():#Ако се напише в промеливатата енд независимо то големината на буквите принтира колко човек са в листа един под друг
        remaining_people = len(opashka)#минава списака елемент по елемент и дава число
        if remaining_people > 0:
            for people01 in opashka:# да ги принтира един под друг
                print(people01)
            print(f"{remaining_people} people remaining.")#колко човека са написани след енд като бройка
        else:
            print("0 people remaining.")
        break
    
    elif klienti == "PAID".lower():#тези които са платили
        while opashka:
            print(opashka.pop(0))
    else:
        opashka.append(klienti)#показва всички платили

