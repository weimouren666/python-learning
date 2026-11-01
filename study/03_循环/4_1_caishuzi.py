answer = 66
while True:
    guess = int(input("猜答案"))
    if guess == answer:
        print("恭喜你猜对了")
        break
    elif guess < answer:  
        print("猜小了")  
    else:
        print("猜大了")    