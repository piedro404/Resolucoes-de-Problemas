def calcMatriz(list, l, func):
    s = sum(list[l])

    if(func == "M"):
        s /= len(list[l])

    return float(s)

l = int(input())
func = input()
list = []
for x in range(12):
    listT = []
    for x in range(12):
        listT.append(float(input()))
    
    list.append(listT)

print("{:.1f}".format(calcMatriz(list, l, func)))