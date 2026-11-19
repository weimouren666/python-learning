text = "python is great and data is great and python is fun"
def count_words(text):
    count = {}
    for w in text.split():
        count[w] = count.get(w,0) + 1
    return count
def most_frequent(count):
    best_w, best_n = "",0
    for w, n in count.items():
        if n > best_n:
            best_w, best_n = w, n
    return best_w, best_n 
def distinct(word):
    return len(set(words))
words = text.split()
count = count_words(text)               
word, n = most_frequent(count)          
print("词频：", count)
print(f"出现最多：{word}，{n} 次")        
print(f"不同单词：{distinct(words)} 个")                 