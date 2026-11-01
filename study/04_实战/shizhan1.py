#拿取bmi计算相关条件
name = input("输入你的名字: ")
xingbie = input("输入你的性别: ")
nianling = int(input("输入你的年龄: "))
height = float(input("以米为单位输入你的身高: "))
weight = float(input("以千克为单位输入你的体重: "))
bmi = weight / (height ** 2)
bmi = round(bmi,2)
#给出体型建议
if bmi < 18.5:
    tixing = "偏瘦"
    print(f"{name},你的体型偏瘦 ，应该增加优质蛋白与主食，配合力量训练增肌")
elif bmi >= 18.5 and bmi < 24:
    tixing = "正常"
    print(f"{name},你的体型正常 ，应该保持规律作息，每周 3 次中等强度运动")
elif bmi >= 24 and bmi < 28:
    tixing = "超重"
    print(f"{name}你的体型超重，应该减少精制碳水与含糖饮料，先不急着节食")
else:
    tixing = "肥胖"
    print(f"{name},你的体型肥胖，应该咨询专业营养科，循序渐进减重")
#健康卡片
print("================================")
print("          个人健康卡片")
print("================================")
print(f"姓名: {name}")
print(f"性别：{xingbie}")
print(f"年龄: {nianling} 岁")
print(f"身高: {height} m")
print(f"体重:{weight} kg")
print(f"BMI:{bmi}")
print(f"体型: {tixing}")
print("================================")
