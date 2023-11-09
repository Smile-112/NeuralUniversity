def inseq(seq):
    if seq.find(".") != -1:
        seq = seq.split(".")
    elif seq.find(",") != -1:
        seq = seq.split(",")
    else:
        seq = seq.split("/")
    ans = []
    for i in seq:
        if seq.count(i) == 1:
            ans.append(int(i))
    return ans


arr1 = inseq(input('Введите элементы первого списка (подряд):\n'))
arr2 = inseq(input('Введите элементы первого списка (подряд):\n'))
arr3 = []

for i in arr1:
    if i not in arr2: arr3.append(i)
print(arr3)