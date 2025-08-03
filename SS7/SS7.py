## thử với vòng lặp vô hạn
# i = 10
# while i > 0:
#     print(i) # 10, 9, .... 1
#     i = i - 1 # 9, 8, ... 0


### Chữa bài: Nhật Minh, Hải Nam (++)
# n = int(input("Nhập số nguyên n: "))
# while n < 0 or n > 100: 
#     n = int(input("Nhập số nguyên n: "))

# for i in range(n, 101):
#     print(i)




### Ứng dụng Number Guessing: Chọn 1 số n: 0 < n < 100 => Tối đa 5 lần đoán để tìm ra n.
import random

secret_number = random.randint(1, 100)
guesses_taken = 0
max_guesses = 7
while guesses_taken < max_guesses: 
    # Yêu cầu người chơi đoán số
    guess = int(input(f"Lượt đoán {guesses_taken + 1}. Mời bạn đoán số: "))
    
    # Tăng lượt đoán
    guesses_taken += 1
    
    if guess < secret_number:
        print("Số của bạn nhỏ quá! Hãy thử một số lớn hơn.")
    elif guess > secret_number: 
        print("Số của bạn lớn quá! Hãy thử một số nhỏ hơn.")
    else:
        #Đoán đúng
        print(f'Chúc mừng! Bạn đã đoán đung số {secret_number} trong {guesses_taken} lượt đoán!')
        

print(f'Bạn đã hết {max_guesses} lượt đoán. Số bí mật là {secret_number}.')
print("Chúc bạn may mắn lần sau")
