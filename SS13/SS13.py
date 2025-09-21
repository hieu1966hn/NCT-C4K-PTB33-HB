# ## Hàm không có giá trị trả về 
# def dien_tich_can_phong(a, b):
#     print(f"Diện tích căn phòng là: {a*b}")
#     return a*b
    
# # Gọi hàm:
# S_phong = dien_tich_can_phong(30, 25) # 750

# ## Hàm có giá trị trả về
# def so_luong_tam_gach(dien_tich_can_phong):
#     dien_tich_tam_gach = 20*20/100
#     return dien_tich_can_phong/dien_tich_tam_gach

# print(f"Số lượng viên gạch cần cho căn phòng là: {so_luong_tam_gach(S_phong)}")
    
    
## Bài thực hành luỹ thừa

# def tinh_luy_thua(a, b):
#     return a**b # a^b

# a = int(input("nhập số a: "))
# b = int(input("nhập số b: "))
# # Gọi hàm
# print(f"Luỹ thừa {a}^{b} là: {tinh_luy_thua(a,b)}")


# def tri_tuyet_doi(n):
#     if n < 0:
#         return -n
#     else:
#         return n

# print(tri_tuyet_doi(-1))



# Thực hành với danh sách:
# def sum_list(arr: list): # [1 ,2 ,3]
#     sum = 0
#     for value in arr:
#         sum += value # 6
#     return sum 

# print(sum_list([1,2,3]))

# Kết nối tới thư viện Math của Python

# import math
# from math import gcd
# print(gcd(5, 10)) # UCLN: 5

# print(1 + abs(-1))

# print(pow(4,5))

# import random
# print(random.random()*100) 
# print(random.randint(1, 10))


def tinh_luong(gio_lam, luong_gio):
    tong_luong = gio_lam * luong_gio
    return tong_luong

def in_thong_tin(ten, gio_lam, luong_gio):
    print(f"Tên: {ten}")
    print(f"Số giờ làm: {gio_lam}")
    print(f"Mức lương theo giờ: {luong_gio}")
    print(f"Tổng lương: {tinh_luong(gio_lam, luong_gio)}")
    
ten = "Nguyễn Trung Hiếu"
gio_lam = 160
luong_gio = 20000

print(in_thong_tin(ten, gio_lam, luong_gio))
    
    