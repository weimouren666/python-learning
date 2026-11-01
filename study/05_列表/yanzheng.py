scores = [88, 92, 76, 59, 100]

print(scores[0], scores[1], scores[2])   # 88 92 76 —— 下标从0
print(scores[-1])                         # 100 —— 负下标倒着数
print(scores[5])                          # 看它报什么错！读一遍报错信息# print(scores[5])    # 已验尸完毕，注释掉让程序继续
print(scores[1:3])                        # [92, 76] —— 含头不含尾
scores.append(95)
print(scores)                             # [88, 92, 76, 59, 100, 95]
print(len(scores))                        # 6
print(sorted(scores, reverse=True))       # [100, 95, 92, 76, 59, 88, ...]
print(85 in scores, type(85 in scores))   # False <class 'bool'>
