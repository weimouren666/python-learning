#问身高
h = input("输入你的身高:")
h = float(h)
#问体重
w = input("输入你的体重:")
w = float(w)
#计算 BMI = 体重 ÷ 身高的平方
BMI = w / (h * h)
print(f"你的BMI是{BMI}")

