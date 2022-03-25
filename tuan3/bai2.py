def calculate(td1, td2):
    x1 = td2[0] - td1[0]
    y1 = td2[1] - td1[1]
    pt = (-y1, x1)

    c = pt[0]*td1[0] + pt[1]*td1[1]
    return (pt[0], pt[1], c)

result = calculate((2, 3), (6, 4))
print("ket qua cua a, b, c lan luot la: ")
print(result)