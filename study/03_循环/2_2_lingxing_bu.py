n=int(input("输入菱形高度："))
#上半部分
for i in range(1 , n + 1):
    print(" "*(n - i) + "*"*(2 * i - 1))
#下半部分
for i in range(n - 1, 0 , - 1):
    print(" "*(n - i) + "*"*(2 * i - 1) )   