import random        #引入random
answer = random.randint(1,100)
print("我已经想好一个1到100之间的数了")
count = 0
while True:
    guess=int(input("来猜一下吧："))        #输入猜的数值
    count=count + 1        #累计猜的次数
    if guess == answer:
        print(f"你猜中了，一共猜了{count}次")
        break
    elif guess <answer:
        print(f"你猜小了") 
    else:
        print(f"你猜大了")       