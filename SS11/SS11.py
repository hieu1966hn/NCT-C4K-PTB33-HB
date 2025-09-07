# a = "MindX"
# print(len(a)) # 5
# print(a[0]) # M
# print(a[len(a) - 1]) # X


# A = ['a', 'b', 'c', 'd'] # Danh sachs
# B = "abcd" # Chuỗi ký tự

# # Nhiệm vụ chung: Cập nhật a => f
# A[0] = 'f'
# B[0] = 'f'  # err => chuỗi ký tự không thay đổi được các giá trị bên trong

# print(A)
# print(B)

# M = "MindX Technology"
# Duyệt xâu M
# C1: Duyệt xâu theo giá trị i
# for i in M:
#     print(i)
    
# # C2: Duyệt xâu theo vị trí ký tự
# for j in range(len(M)): # M = "abc" range(len(M)) => 0 - 2
#     if M[j] != " ": # Kiểm tra nếu không phải dấu " " => chạy code
#         print(M[j], end="") # end="": dùng để print thành 1 hàng



#### Module 2: Xâu con và tìm vị trí của xâu con
# s = "abcd123"
# a = 'abc'
# b = "d12"
# c = "1234"


# ### Kiểm tra a, b có là xâu còn của s không?
# if a in s: # True/ False
#     print("Xâu a nằm trong xâu s")
# else:
#     print("Xâu a không nằm trong xâu s")
    
# x = s.find(b) # kết quả trả về vị trí xâu con trong xâu cha (nếu không có trả về -1)
# print(x) # 0: Vị trí bắt đầu của xâu con 


### Module: Lệnh thường dùng với xâu ký tự

# s = "a b c d1 234"
# x = s.split(" ") # Tách chuỗi ký tự thành danh sách theo dấu " "
# print(x) ## ?


# s2 = "1,2,3,4,5"
# x = s2.split(",")
# print(x) #


# txt = "Hello Việt Nam"
# x = txt.replace("Việt Nam", "Everyone")
# print(x) # Hello Everyone

### Module thực hành

### Đề 1: Viết một chương trình nhập vào Họ và tên vào 2 biến khác nhau
##1.  Sau đó in ra màn hình họ và tên vừa nhập
##2.  Ghép 2 biến thành 1 xâu ký tự

# ho = input("Nhập vào họ: ")
# ten = input("Nhập vào tên: ")
# print("Họ và tên đầy đủ là: ", ho + " " + ten)


### Chữa bài 1:
# dmy = input("Nhập ngày tháng năm theo định dạng dd/mm/yyyy: ") # 07/09/2025
# x = dmy.split("/")
# print(f'"Ngày {x[0]} tháng {x[1]} năm {x[2]}"')


### Chữa bài 2: 
# Tạo tài khoản có sẵn
account = "MindX:12345"

# Tách username và pass từ chuỗi trên
x = account.split(":")
username = x[0]
password = x[1]

while True:
    # người dùng nhập thông tin đăng nhập
    user_input = input("Nhập username: ")
    pass_input = input("Nhập password: ")
    
    # kiểm tra
    if user_input == username and pass_input == password:
        print("Đăng nhập thành công!")
        break # Thoát vòng lặp
    else:
        print("Thông tin đăng nhập chưa chính xác, vui lòng thử lại. \n")
