# Tạo danh sách đầu tiên

n = [10, 0, 1, 9 , 8] # Danh sách có 2 phần tử


## Số phần tử trong danh sách được đếm bằng: len(n)
# print(len(n))

# In ra vị trí số 0 trong danh sách 
# print(n[0]) # 10

# in ra vị trí cuối cùng trong danh sách
# print(n[len(n) - 1]) # n[4] = 8

# Sửa giá trị khi biết vị trí trong list 9 -> 99
# n[3] = 99 
# print("Danh sách được cập nhật 3 => 99", n)

## Thêm 1 phần tử vào cuối danh sách list.append()
n.append(100) 
print("Danh sách được thêm 100 vào cuối", n)

## Thêm 1 phần tử vào vị trí cụ thể: 
n.insert(1, "index 1")
print("Chèn giá trị vào vị trí số 1", n)

# Xoá phần tử trong danh sách: cần biết giá trị
n.remove(0)
print("Đã xoá giá trị số 0", n)

# Xoá phần tử khi biết vị trí: vị trí số 1
del n[1]
print('Đã xoá giá trị ở vị trí số 1', n)