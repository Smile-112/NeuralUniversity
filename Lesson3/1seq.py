num = int(input('Введите кол-во чисел в списке: '))
arr = []
for i in range(num):
    arr.append(int(input()))
print(sorted(arr))
