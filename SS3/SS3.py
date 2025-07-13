# ## ôn tập lại kiến thức buổi 2 => Kiến thức buổi 3


# ##### Buổi 2
# ## Tìm hiểu về biến: 
# a = 100 ## a là tên vùng nhớ được đặt - 100 là giá trị bên trong vùng nhớ đó
# be_ca = "cá" ## be_ca là tên vùng nhớ là bể cá - "cá" là giá trị bên trong vùng nhớ đó.

# print(a, be_ca) ## 100 - Cá

# a = 10
# be_ca = "Cá Mập"

# print(a, be_ca) ## 10 - Cá Mập



# ### Các kiểu dữ liệu trong Python
# ## 1. Kiểu số nguyên: int. VD: 
# a = 1
# b = 2
# c = 123

# ## 2. Kiểu số thực: float. VD: 
# d = 12.5
# e = .9 # 0.9
# f = 12.0 

# ## 3. Kiểu chuỗi: string. VD
# k = "Hello World!!"

# ## 4. Kiểu Boolean: bool. VD
# y = True  
# x = False
# i = 1 + 1 > 3
# print(i) ## True/False



# ##### Chuyển đổi các kiểu dữ liệu 
# age = input("Xin hãy nhập tuổi của bạn: ") 

# # kiểm tra xem age đang là kiểu dữ liệu gì?
# print(type(age)) ## kiểu dữ liệu gì? String

# # chuyển đổi chuỗi => số
# age = int(age)

# future_age = age + 10 
# print("Trong 10 năm tới, bạn sẽ", future_age, "tuổi")



######## Kiến thức buổi 3: Tính toán toán tử
#### Toán tử số học:  thao tác kết hợp các giá trị tạo ra một giá trị với. VD: +, - , *, /
# a = 1
# b = 2
# ## phép cộng
# print(a + b)# 3

# ## phép trừ
# print(a - b)# -1

# ## phép nhân
# print(a * b)# 2


# ## phép chia
# print(a / b)# 0.5

# # phép chia lấy dư %
# print(a % b) # 1

# # phép chia lấy nguyên
# print(a // b) # 0

# # phép + với chuỗi  => để nối 2 chuỗi ký tự với nhau
# print("Hello " + "World!!") # Hello World!!

# # phép * với chuỗi => 
# print("hi"*3) ## 


###### Toán tử quan hệ (so sánh):  => True/False
# print(1>2) # False
# print(2<3) # True
# print(3 >= 3) # True
# print(2 <= 3) # True
# print(4 == 4) # True
# print(1 != 0) # True


#### Toán tử logic:  
## Toán tử OR: 5 >= 5 ===> 5 == 5 hoặc 5 > 5
print(5>5 or 5==5) ## False or True ==> True
print(5>5 or 5<5) ##  False or False ==> False


## Toán tử AND: 
print(1 < 2 and 3 < 4) ## True and True => True
print(1 < 2 and 3 > 4) ## True and False => False

### test kiến thức
x, y, z = 10, 6, 8

a = x < 12 and z > 6 # True
b = x > 15 or y < 8 # True
c = not b # False

print(a, b, c)
