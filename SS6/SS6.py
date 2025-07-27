## In ra các số theo yêu cầu
# for i in range(6):
#     print(i) # 0, 1, 2, 3, 4, 5


# for i in range(3, 10,  2):
#     print(i) # 3, 5, 7, 9



# ##### Bài tập tính tổng các số chẵn
# a = int(input("Người dùng nhập số nguyên a: "))
# b = int(input("Người dùng nhập số nguyên b: "))

# ## a -> b => range(a, b) - (phạm vi) 
# sum = 0 # lưu tổng các số chẵn
# for i in range(a,b): # 10 - 1
#     # tính tổng các số chẵn 3 - 10
#     if i%2 == 0:
#         sum = sum + i

# print(sum)


# #### Bài tập in bảng cửu chương từ 2 - 9
# for i in range(2, 10): # 2 - 9
#     for j in range(1, 11): # 1 - 10
#         print(f"{i} x {j} = {i*j}")
        


## Đề bài thực hành: 
# Nhập vào chiều dài - rộng của HCN yêu cầu:
# - Vẽ hình chữ nhật bằng các ký tự *

# width = int(input("Nhập chiều rộng HCN: ")) # 3
# height = int(input("Nhập chiều cao HCN: ")) # 3

# for i in range(height): # 0 - height
#     print("*"*width)
        
        
## Đề bài: Nhập n, tính n! (giai thừa của n)
## 4! = 1 * 2 * 3 * 4; 5! = 1*2*3*4*5
n = int(input("Nhập n: "))
giai_thua = 1
if n<0: 
    print("Không tồn tại giá trị n < 0")
elif n == 0:
    print(f"{n}! = {1}")
else:
    for i in range(1, n+1):
        giai_thua *= i

print(giai_thua)

        
    
