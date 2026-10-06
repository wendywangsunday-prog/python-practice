def calc_average(numbers):
    #定義平均值怎麼算
    if not numbers:
        return 0.0

    total=0
    for a in numbers:
        total+= a
    return total/len(numbers)

        
#主程式：取得使用者輸入並轉換成list
user_input = input("請輸入數字（用空格隔開）：")
scores = [float(x) for x in user_input.split()]#將輸入字串用空格切開，並逐一轉換成float放進list

#呼叫韓式並印出結果
avg = calc_average(scores)
print(f"輸入的List為：{scores}")
print(f"計算出的平均值為：{avg:.2f}")

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"
    
user_input = input("請輸入分數：")
score_val = float(user_input)#換型態

grade = get_grade(score_val) #傳入函式
print(f"分數：{score_val} -> 等第：{grade}")


def square(n):
    return n**2

def is_even(n):
    return n%2 == 0 # ==本身就會回傳true,false

def greet(name, greeting='Hello'):
    return f"{greeting},{name}!"

def min_max(numbers):
    return min(numbers), max(numbers)

num = 5
print(f"{num}的平方是：{square(num)}")

print(f"4是偶數嗎？ {is_even(4)}")
print(f"7是偶數嗎？ {is_even(7)}")

print(greet("wendy"))
print(greet("wendy","good morning"))

lo, hi = min_max([3,1,9,5,2])
print(f"最小值 lo:{lo}, 最大值 hi:{hi}")

def count_pass(scores, passing=60):
    count = 0
    for a in scores:
        if a >= passing:
            count +=1
    return count

score_list = [55,60,88,42,95]
print(f"及格人數（預設60分)：{count_pass(score_list)}")
print(f"高分人數（自訂80分）：{count_pass(score_list,80)}")

def filter_even(numbers):
    even_list = []
    for a in numbers:
        if a % 2 == 0:
            even_list.append(a)
    return even_list

raw_nums = [1,2,3,4,5,6]
print(f"偶數list:{filter_even(raw_nums)}")

#cat
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char+reversed_s
    return reversed_s

text = "Python"
loop_result = reverse_string(text)
slice_result = text[::-1] #留空：從最右邊（開始），直到最開頭（結束） 
print(loop_result)
print(slice_result)

def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count+=1
    return count

sample_text = "Hello World! Python is Awesome."
print(f"文字：{sample_text}")
print(f"母語數量：{count_vowels(sample_text)}")

#fizzbuzz(n)：3 的倍數回傳 "Fizz"，5 的倍數回傳 "Buzz"，同時是兩者的倍數回傳 "FizzBuzz"，
# 其他回傳數字本身。再寫迴圈印出 1 到 20 的結果。
def fizzbuzz(n):
    if n%3 == 0:
        return "Fizz"
    elif n%5 == 9:
        return "Buzz"
    elif n%3 ==0 & n%5==0:
        return "FizzBuzz"
    else:
        return str(n)

print ("===1到20的結果===")
for i in range(1,21):
    print(f"{i}:{fizzbuzz(i)}")

#score_report(scores)：自己寫一個函式，呼叫你之前寫的 calc_average 和 get_grade，
# 回傳類似 平均 84.2，等級 B。

def score_report(scores):
    avg = calc_average(scores)
    grade = get_grade(avg)

    return f"平均{avg:.1f},等級{grade}"

my_scores = [85, 92, 78,88,79]
report = score_report(my_scores)
print(f"成績：{my_scores}")
print(f"成績報告：{report}")