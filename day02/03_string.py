#練習 3：字串處理（03_string.py）
#用 text = "  Hello, Python World  "：
#用 .strip() 去除前後空白。
#用 .lower()、.upper()、.replace() 各練習一次。
#用 .split() 切成單字 list，再用 " ".join(...) 接回去。
#寫 count_words(sentence)：回傳每個單字出現次數的 dict，例如 "a b a" → {"a": 2, "b": 1}。
#用 f-string 格式化：print(f"{3.14159:.2f}")，試試看小數點兩位的效果。

#1.
text = "      Hello, Python World "
print(text)
print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("World","taiwan"))

#2.
world_list = text.split() #切割字串,回傳list
print(world_list)

rejoined_text = "".join(world_list) #接回去
print(rejoined_text)

#3.
def count_words(sentence):
    words = sentence.split() #先把句子切成單字清單(list)
    word_count = {} #準備一個空字典，紀錄{"單字"：次數}


    #.get(key,預設值)：
    for a in words:
        word_count[a] = word_count.get(a,0)+1 #算出新的出現次數
    return word_count

test_sentence = "apple banana apple orange banana apple"
result = count_words(test_sentence)
print(f"原句子：{test_sentence}")
print(f"單字統計結果：",result)

#4. 
#f"{a:.2f}"
pi =3.14159

print(f"原始pi:{pi}")
print(f"保留小數點兩位：{pi:.2f}")
print(f"保留小數點三位：{pi:.3f}")
pi_pi = f"{pi:.1f}"
print(pi_pi)