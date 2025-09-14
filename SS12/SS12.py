# Khởi tạo hàm - chương trình con đầu tiên
def Hello():
    print("Xin chào, tôi là Hiếu Nguyễn")
    print("Rất vui được gặp bạn")
    
# Gọi hàm để chạy
# Hello()

# HÀM ÉP MÍA
def may_mia():
    print("Ép mía")
    print("Cốc nước mía")
    
# may_mia()

## Đề bài 1: Viết hàm nhập vào họ và tên rồi đưa ra lời chào ra màn hình
def say_hello():
    full_name = input("Nhập vào họ và tên của bạn")
    print(f'Xin chào {full_name}')

# Gọi hàm
# say_hello()
# say_hello()
    
## Đề bài 2: Hàm nhập vào số nguyên, xuất ra màn hình giá trị tuyệt đối của số nguyên vừa nhập
def tri_tuyet_doi():
    number = int(input("Nhập vào số nguyên: "))
    if number < 0: 
        number = -number
    print(f"giá trị tuyệt đối của số nguyên là: {number}")
    
# tri_tuyet_doi()



### VÍ DỤ HÀM CÓ THAM SỐ: 
ho_va_ten = 'Nguyễn Trung Hiếu'
def say_hello_v2(full_name): # truyền họ và tên vào hàm để sử dụng. => THAM SỐ: Biến được định nghĩa trong hàm
    print(f"Xin chào {full_name}")
    
# Gọi hàm
# say_hello_v2(ho_va_ten) # => Đối số: Giá trị thực tế truyền vào cho tham số khi gọi hàm.


# THỰC HÀNH 3: Chương trình tính tổng 2 số truyền vào
def sum(a, b):
    print(f'Tổng của {a} và {b} là: {a+b}')
    
sum(2, 3)# 2 sẽ được gán với biến a || 3 sẽ được gán với biến b


## THỰC HÀNH 4: Chương trình nhập vào một danh sách số nguyên, 
# sử dụng hàm để xuất ra các phần tử của list vừa nhập và tổng của list đó
def in_danh_sach_va_tong(danh_sach): # [1, 3 ,5 ,7 ,9]
    tong = 0
    for so in danh_sach:
        tong += so
        print(so)
    print(f"Tổng của list là: {tong}")
    
# in_danh_sach_va_tong([1, 3 ,5 ,7 ,9])


### Module 4: phạm vi biến: cục bộ - toàn cục
# c = 10 # KHỞI TẠO BIẾN C
# def test():
#     a = 1
#     b = 2
#     global c # lấy ra biến toàn cục từ bên ngoài để sử dụng và thay đổi
#     c = "BIẾN TOÀN CỤC" # 10 -> "BIẾN TOÀN CỤC" (chỉ cập nhật bên trong hàm thôi)

# print(c) # in được: Giữ nguyên giá trị
# print(a, b) # lỗi


### ĐỀ BÀI VÒNG QUAY MAY MẮN 1: Tổng các số chia hết cho 2 trong 1 list
arr = [1, 4, 70, 100, 50,0 , 9]
# def tong_so_chia_het_cho_2(arr):
#     tong = 0
#     for so in arr:
#         if so % 2 == 0: # %: phép chia lấy dư
#             tong += so
#     print(f"Tổng các số chia hết cho 2 trong danh sách là: {tong}")
    
# tong_so_chia_het_cho_2(arr)
            
# ĐỀ bài vòng quay may mắn 2:  Tìm ra số bé nhất
# def tim_min(arr):
#     min = arr[0]
#     for so in arr:
#         if min > so:
#             min = so
#     print(f'Số bé nhất trong danh sách là: {min}')

# tim_min(arr)


### Tính trung bình cộng của các số trong danh sách
## arr = [1, 4, 70, 100, 50,0 , 9]
def trung_binh_cong(arr):
    tong = 0
    for so in arr:
        tong += so
    print(f'Trung bình cộng của danh sách là: {tong/len(arr)}')
    
trung_binh_cong(arr)