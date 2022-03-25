def Calculate(A, B, C):
    x1 = B[0] - A[0]
    y1 = B[1] - A[1]
    z1 = B[2] - A[2]
    vt1 = (x1, y1, z1)

    x2 = C[0] - A[0]
    y2 = C[1] - A[1]
    z2 = C[2] - A[2]
    vt2 = (x2, y2, z2)

    x = vt1[1]*vt2[2] - vt2[1]*vt1[2]
    y = vt1[2]*vt2[0] - vt2[2]*vt1[0]
    z = vt1[0]*vt2[1] - vt2[0]*vt1[1]
    pt = (x,y,z)

    d = pt[0]*A[0] + pt[1]*A[1] + pt[2]*A[2]
    return (pt[0], pt[1], pt[2], d) 


result = Calculate((2, 0, 0), (0, -3, 0), (0, 0 ,4))
print("phuong trinh mat phang di qua 3 diem la: ")
print(result)