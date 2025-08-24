## Đề bài 1: Kiểm tra n có phải là số nguyên tố hay không ?
# n = int(input("Nhập n: ")) # 5

# # Kiểm tra xem từ 2 - n có chia hết cho số nào nữa không nếu có => n ko là snt. Ngược lại => n là snt
# for i in range(2, n): # 2 - 4
#     if n % i == 0:
#         print(f"{n} không là số nguyên tố")
#         break # dừng luôn vòng lặp
#     if i == n-1: # Kiểm tra i là lần lặp cuối cùng 
#         print(f"{n} là số nguyên tố")
#         break
    
    
import math # thư viện math của Python
#### Đề bài 2: 
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if b == 0:
    print("Phân số không hợp lệ vì mẫu số bằng 0.")

else: 
    ## Tính UCLN
    UCLN = math.gcd(a, b)

    # Tính BCNN (a, b) = |a*b| // UCLN(a,b)
    BCNN = abs(a*b) // UCLN # Chia lấy phần nguyên 
    print(f"BCNN của {a} và {b} là {BCNN}")
    
    ## Rút gọn phân số : chia cả tử và mẫu cho UCLN để rút gọn
    a_gon = a // UCLN
    b_gon = b // UCLN
    
    # In phân số sau khi tối giản
    print(f'Phân số sau khi tối giản là: {a_gon}/{b_gon}')
    








    
