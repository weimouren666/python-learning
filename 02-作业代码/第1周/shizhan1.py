#拿取bmi计算相关条件
name = input("Please enter your name: ")
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))
bmi = weight / (height ** 2)
#给出体型建议
if bmi < 18.5:
   tixing = "偏瘦"
   print(f"{name},你的体型偏瘦 ，应该增加优质蛋白与主食，配合力量训练增肌")
if bmi >= 18.5 and bmi < 24:
    tixing = "正常"
    print(f"{name},你的体型正常 ，应该保持规律作息，每周 3 次中等强度运动")
if bmi >= 24 and bmi < 28:
    tixing = "超重"
    print(f"{name}你的体型超重，应该减少精制碳水与含糖饮料，先不急着节食")
if bmi >= 28:
    tixing = "肥胖"
    print(f"{name},你的体型肥胖，应该咨询专业营养科，循序渐进减重")
#健康卡片
print("================================")
print("          个人健康卡片")
print("================================")
print(f"姓名: {name}")
print(f"身高: {height} m")
print(f"体重:{weight} kg")
print(f"BMI:{bmi}")
print(f"体型: {tixing}")
print("================================")
