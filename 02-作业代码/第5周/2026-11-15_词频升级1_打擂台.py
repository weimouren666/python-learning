count = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
best_ch, best_n = "", 0          # 擂台初始：没人、0 次

for ch, n in count.items():      # items() 发卡片，两个变量接一对
    if n > best_n:               # 挑战者比擂主强？
        best_ch = ch           # 占座：谁
        best_n = n            # 占座：几次

print(f"出现最多：{best_ch}，{best_n} 次")
