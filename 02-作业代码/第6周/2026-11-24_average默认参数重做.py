def average(scores, digits=2):
    return round(sum(scores) / len(scores),digits)
print(average([88, 92, 76]))
print(average([88, 92, 76], 1))