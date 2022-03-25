# Nhóm 2
# Lê Thị Thuỳ Dung 20001895 K65A3
# Lưu Hiểu Huy 20001926 K65A3
# Trần Ngọc Hải 20001911 K65A3

# Bài tập 02: Tọa độ trên bàn cờ.

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']

# Bài 1: Kiểm tra tính hợp lệ của tọa độ trên bàn cờ vua

def check_position(pos):
    if len(pos) != 2:
        return False

    first = pos[0:1]
    second = pos[1:2]
    check = 0

    for i in columns:
        if first == i:
            check += 1
            break

    for i in rows:
        if second == i:
            check += 1
            break

    if check == 2:
        return True
    else:
        return False


print('Bài 1')
print(check_position('a1'))  # True
print(check_position('1a'))  # False
print(check_position('A1'))  # False
print(check_position('Aone'))  # False


# --------------------------------------------------------


# BÀI 2: Tọa độ trên bàn cờ.

# Hàm trả về tọa độ của những quân xe
# trong vị trí khởi đầu tiêu chuẩn của một ván cờ vua.
def get_rock_position():
    return 'a1 a8 h1 h8'

print('Bài 2')
print("Tọa độ các quân xe trong vị trí khởi đầu là: ", get_rock_position())

# Hàm trả về tọa độ của 64 ô trên bàn cờ.
def get_64_chequered():
    pos = []
    for i in columns:
        for j in rows:
            elm = i + j
            pos.append(elm)
    return pos

arr = get_64_chequered()
print('Tọa độ 64 ô trên bàn cờ là:')
print(arr)

# Hàm trả về tọa độ của 32 ô trắng trên bàn cờ
def get_white_chequered():
    pos = []
    for i in range(len(columns)):
        for j in range(len(rows)):
            if (i + j) % 2 != 0:
                text = columns[i] + rows[j]
                pos.append(text)
    return pos


array = get_white_chequered()
print("Tọa độ các ô trắng trong bàn cờ:")
print(array)


# --------------------------------------------------------

# Bài 3
# Hàm kiểm tra xem hai ô đưa vào có 
# cùng hàng ngang hoặc cột dọc hay không

def check_in(row, col):
    for i in columns:
        for j in rows:
            if i == row and j == col:
                return True
    return False


def check_insame(text1, text2):
    f1 = text1[0:1]
    s1 = text1[1:2]
    f2 = text2[0:1]
    s2 = text2[1:2]
    if check_in(f1, s1) and check_in(f2, s2):
        if f1 == f2 or s1 == s2:
            return True
    return False

print('Bài 3')
print(check_insame('a1', 'c2')) # False
print(check_insame('a3', 'a7')) # True
print(check_insame('a2', 'c2')) # True


# --------------------------------------------------------

# Bài 4: Nước đi của quân xe


def rock_move(text):
    pos = []
    current_row = text[2:3]
    current_col = text[1:2]
    for i in columns:
        if i == current_col:
            for j in rows:
                if j == current_row:
                    continue
                pos.append(i + j)
            break

    for i in rows:
        if i == current_row:
            for j in columns:
                if j == current_col:
                    continue
                pos.append(j + i)
            break
    return pos

print('Bài 4')
start = 'Ra2'
move = rock_move(start)
print(move)

# --------------------------------------------------------

# Bài 5: Nước đi của quân tượng


def check_position(col):
    for i in range(len(columns)):
        if columns[i] == col:
            return i + 1
    return -1


def bishop_move(text):
    cross = []
    current_row = text[2:3]
    current_col = text[1:2]
    cross1_line = check_position(current_col) + int(current_row)
    cross2_line = 9 - check_position(current_col) + int(current_row)

    for i in range(len(columns)):
        for j in range(len(rows)):
            if (i + j) == cross1_line-2 and columns[i] != current_col and columns[j] != current_row:
                cross.append(columns[i] + rows[j])

            if (7 - i + j) == cross2_line-2 and columns[i] != current_col and columns[j] != current_row:
                cross.append(columns[i] + rows[j])

    print(cross)

print('Bài 5')
start = 'Ba2'
bishop_move(start)
