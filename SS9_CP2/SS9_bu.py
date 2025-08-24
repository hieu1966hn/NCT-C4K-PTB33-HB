# # for i in "hello":
# #     print(i)


# ### Khởi tạo danh sách
# ptb33 = ["Tuệ Khanh", "Trung Hiếu", "Tuệ Minh", 'Nhật Minh','Mai Phong'] # nếu không có phần tử => rỗng
# #           0               1           2           3              4
# ## Số phần tử trong danh sách: len()
# print(len(ptb33)) # 5

# # Truy cập phần tử vị trí số 0, 3, 4: 
# print(ptb33[0]) #  Tuệ Khanh
# print(ptb33[3]) #  ..
# print(ptb33[len(ptb33) - 1]) # Mai Phong (vì là phần tử cuối cùng)


# ## Cập nhật giá trị Tuệ Khanh => Tuệ Khanh xinh đẹp
# ptb33[0] = "Tuệ Khanh xinh đẹp"
# print(ptb33)


# # thêm phần tử vào cuối danh sách: append
# ptb33.append("Hải Nam")
# print(ptb33) ## Đã được thêm bạn mới



#### Bài thực hành tổng hợp:
## Nhập vào danh sách các bạn trong lớp PTB33.
# Nhập liên tục tên các bạn trong danh sách. Nhập "E" để kết thúc chương trình

ptb33 = []
ban_moi = input("Nhập tên học sinh: ")
while ban_moi != "E": 
    ptb33.append(ban_moi)
    # Thêm bạn mới vào cuối danh sách PTB33
    ban_moi = input("Nhập tên học sinh: ")

print(f"Kết thúc chương trình. Danh sách học viên lớp PTB33 là: {ptb33}")

