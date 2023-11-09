def guess(time, part):
    match part:
        case 1:
            while time!= 1799:
                print("Не верно")
                time = int(input('Ввведите год рождения А.С.Пушкина: '))
            print('Верно')
            return True
        case 2:
            while time != 6:
                print("Не верно")
                time = int(input('В какой день июня родился Пушкин? '))
            print('Верно, Поздравляем!')
            return True

if guess(int(input('Ввведите год рождения А.С.Пушкина: ')),1): guess(int(input('В какой день июня родился Пушкин? ')),2)