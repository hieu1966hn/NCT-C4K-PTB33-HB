# # ### Duyệt phần tử: ?
# # # A = [2, 4, 6, 8 ,10, 12]
# # ## Duyệt danh sách với vòng lặp for

# # ## C1: Duyệt từng phần tử
# # # for i in A:
# # #     print(i) # 2, 4 ,.... 12

# # ## C2: Duyệt theo vị trí
# # # for i in range(len(A)):
# # #     A[i] = A[i] * 2 # dòng này sẽ cập nhật giá trị luôn trong list A
# # #     # print(A[i]) # 2, ... 12
    
# # # ## Tăng giá trị mỗi phần tử trong A lên gấp 2.
# # # print(A)


# # ### Thao tác với danh sách: 
# A = [1 ,2 ,3]

# # Thêm phần tử vào cuối danh sách: list.append()
# A.append(4)
# # print(F"Phần tử mới thêm là: {A[3]}")

# # Thêm vào đầu danh sác hoặc các vị trí khác: list.insert(<vị trí>, <giá trị phần tử thêm>)
# A.insert(0, 0)
# # print(F"Phần tử trong danh sách là: {A}")


# ### CRUD: Create (append, insert), Read (for), Update (arr[i] = , for), Delete: (del, remove)
# del A[2]
# # print(f'Đã xoá phần tử khỏi danh sách: {A}')

# ## Sắp xếp phần tử trong danh sách: list.sort()
# A.sort() # từ nhỏ => lớn
# A.sort(reverse=True)
# print("Danh sách được sắp xếp đảo ngược là:", A)


#### Bài tập thực hành: Shopping Cart
product_list = ["Quần", 'Áo', 'Giầy', 'Thắt lưng', 'Tất', 'Váy']
shopping_cart = []

while True: 
    print("=========== SHOPPING CART ==============")
    print("1. Xem danh sách sản phẩm")
    print("2. Xem giỏ hàng")
    print("3. Thêm sản phẩm vào giỏ hàng")
    print("4. Xoá sản phẩm ra khỏi giỏ hàng")
    print("5. Thoát")
    
    choice = input("Nhập lựa chọn của bạn (1 - 5): ")
    if choice == "1":
        print("========= MENU =========")
        for index, item in enumerate(product_list):
            print(f'{index + 1}. {item}')
    
    elif choice == '2':
        if not shopping_cart: # nếu rỗng
            print("Giỏ hàng của bạn đang trống.")
        else: 
            print("Các mặt hàng trong giỏ hàng của bạn là: ")
            for index, item in enumerate(shopping_cart):
                print(f'{index + 1}. {item}')
    
    elif choice == '3':
        print("========= DANH SÁCH SẢN PHẨM HIỆN TẠI LÀ =========")
        for index, item in enumerate(product_list):
            print(f'{index + 1}. {item}') 
        
        add_item = int(input("Nhập chỉ mục bạn muốn thêm vào giỏ hàng: ")) - 1 # để đúng với vị trí tính từ 0
        # thêm vào đầu giỏ hàng
        shopping_cart.insert(0, product_list[add_item])
    
    elif choice == "4":
        print("Các mặt hàng hiện có trong giỏ hàng là: ")
        for index, item in enumerate(shopping_cart):
            print(f'{index + 1}. {item}')

        index_delete = int(input("Nhập chỉ mục sản phẩm bạn muốn xoá khỏi giỏ hàng")) - 1
        print(f"{shopping_cart[index_delete]} được xoá khỏi giỏ hàng của bạn.")
        del shopping_cart[index_delete]
    
    elif choice == '5':
        break
    else: 
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            
    
            
        