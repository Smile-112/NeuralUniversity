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


print('Введите числа через разделитель:\n')
print(inseq(input()))
