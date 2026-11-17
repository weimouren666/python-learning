#成绩等级判定
score = int(input(" 请输入你的成绩："))
if score >= 90:
    level = "优秀"
elif score >= 80:
    level = "良好"
elif score >=60:
    level = "及格"
else:
    level = "需要加强"
print(f"这次的成绩是{score}，等级为{level}")            