rainbow = ["каждый", "охотник", "желает", "знать", "где", "сидит", "фазан"]
print(" ".join(rainbow))

purchases = [1200, 800, 468, 235, 5800, 1350, 110, 243,
             767, 3500, 5400, 4389, 3690, 2420, 894,
             1766, 2100, 450, 328, 1890, 233, 766, 1765,
             237, 679, 1983, 389, 1760, 2100, 253, 789]

summ = 0
i = 0
while i < len(purchases):
    summ += purchases[i]
    i += 1
print(f"Траты за месяц составили: {summ} рубля")

summ = 0
for i in purchases:
    summ += i
print(f"Траты за месяц составили: {summ} рубля")

print(f"Траты за месяц составили: {sum(purchases)} рубля")


def del_from_tuple(tpl: tuple, elem: vars()):
    tpll = (list(tpl))
    tpll.pop(tpl.index(elem))
    return tuple(tpll)


print(del_from_tuple((1, 2, 3), 1))

phrase = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"
print(f"Количество символов во фразе до буквы \"е\": {phrase.find('е')}")


def to_list(*args):
    return list(*args)


print(to_list((1, "123", 33, 4.5)))
