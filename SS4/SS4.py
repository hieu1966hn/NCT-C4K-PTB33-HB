### Thực hành với bài toán in ra số chẵn lẻ
# num = int(input("Nhập một số nguyên dương: ")) ## 4

# # KIỂM TRA SỐ CHẴN
# if num % 2 == 0: # if True
#     print(num, "Là số chẵn")
# else: 
#     print(num, "Là số lẻ")


##### Thực hành bài toán phân loại quả
# a= 'táo' # giỏ A
# b = 'cam' # giỏ B
# c = 'xoài' # giỏ C
# a = 'Dưa hấu'  # thay đổi loại quả để phân loại phù hợp

# if a == 'táo':
#     print(a, "vào giỏ A")
# elif a == 'cam': # shift + alt + xuống
#     print(a, "vào giỏ B")
# elif a == 'xoài': 
#     print(a, "vào giỏ C")
# else: 
#     print(a, "vào giỏ D")


#### Thực hành bài toán kiểm tra tam giác
a, b, c = 3, 7, 8
if a+b>c and a+c>b and b+c>a:
    print(a,b,c, "là 3 cạnh của tam giác")
else:
    print(a,b,c, "không là 3 cạnh của tam giác")

