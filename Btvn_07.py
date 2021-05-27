# Bài 1:
# Bài 01. Viết chương trình tính tổng, tích của các phần tử trong một list.
# Bài làm:
"""
a_list = [1,23,4,5,56,43,22,11]
tong = 0
tich = 1
for i in a_list:
    tong += i
    tich *= i
print(tong)
print(tich)
"""
# Bài 02. Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
# Bài làm:
"""
list_n = [1,2,3,4,6,7,8,11,-2]
if list_n:
    max = list_n[0]
    min = list_n[0]
    for i in list_n:
        if i > max:
            max = i
        elif i < min:
            min = i
    print(f"giá trị lớn nhất của list_n là {max}")
    print(f"Giá tri nhỏ nhất của list_n là {min}")
else:
    print("Đây là chuỗi rỗng")
"""
#Bài 03. Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
# Bài làm:
"""
list = ["python", "java", "c#", "javascrip", "c/c++"]
j = " program"
# Cách 1:
print([i + j for i in list])
# Cách 2:
for i in range(len(list)):
   list[i] += j
print(list)
"""
# Bài 04. Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
# Bài làm:
"""
n = [1,2,3,4,5,6,7,8,9,0]
x = int(input("nhập x ="))
# Cách 1:
if x >= len(n) or x <= 0:
    print("Bạn đã nhập sai, vui lòng hập lại x!")
else:
    n1 = n[:x]
    n2 = n[x:]
    print(n1)
    print(n2)
# Cách 2:
n1 = [n[i] for i in range(x)]
n2 = [n[i] for i in range(x,len(n))]
print(n1)
print(n2)
"""
# Bài 5:
"""
Bài 05. Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
"""
# Bài làm:
"""
n = [1,2,3,4,5,6,7,8,9,0,3,4,3,5,6,2,2,4,3,2]
count_max = n.count(n[0])
for i in n:
    if n.count(i) > count_max:
        count_max = n.count(i)
for i in n:
    if n.count(i) == count_max:
        print(i)
"""
# Bài 6:
"""
Bài 06. Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
"""
# Bài làm:
"""
list = ["nguyen van tien","nguyen van hung", "do tuan anh","nguyen binh minh", "chu quoc chi"]
dem = 0
for i in list:
    if len(i) >= 2 and i[0] == i[len(i) -1]:
        dem += 1
print(dem)
"""
# Bài 7:
# Bài 07. Viết chương trình kiểm tra 2 list có phần tử chung hay không.
# Bài làm:
"""
n = [1,2,3,4,5,5767,8,9,0]
m = [11,567,7,65]
i = 0
while i <= (len(n) -1):
    if n[i] in m:
        print('2 biến có phần tử chung')
        break
    else:
        if i == len(n) - 1:
            print(" 2 list ko có phần tử chung")
    i += 1
"""

# Bài 8:
""" 
Bài 08. Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
"""
# Bài làm:
"""
A = [1,2,3,4,2,1]
dem = 0
for i in range(len(A)):
    for j in range(i +1,len(A)):
        if A[i] > A[j]:
            dem +=1
print(dem)
"""
# Bài 9:
# Bài 09. Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
# Bài làm:
"""
n = [[1,2,3],[4,5,6],[7,8,9]]
m = [[1,2,3],[3,2,1],[4,5,6]]
a = n[1][1] * (n[2][2]*n[3][3] - n[2][3] * n[3][2])
b = -n[1][2] *(n[2][1]* n[3][3] - n[2][3]*n[3][1])
c = n[1][3] *(n[2][1]*n[3][2] - n[2][2]* n[3][1])
f_n = a  + b + c
print(f_n)
"""
# Bài 10:
"""
Mô tả:
Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
"""
# Bài làm:
"""
n = ["a","b","c","d","e","f","g","h","i","k","a",'b',"t","u","v"]
n1 = []
n2 = []
for i in range(1,len(n)):
    if n[i] not in n[:i]:
        n2 += n[i]
        n1.append(n[i])
print(n1)
print(n2)
"""
"""
n = ["a","b","c","d","e","f","g","h","i","k","a",'b',"t","u","v"]
j = len(n)
i = 1
while i < j:
    if n[i] in n[:i]:
        del n[i]
        j -= 1
        i -= 1
    i += 1
print(n)
"""














