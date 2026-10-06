#dict基本操作
#1. 讀取資料：用[key]
#2. 新增或修改資料：直接指派dict[key]=value
#如果key不存在，會新增這筆資料/如果key已經存在，會修改原本的值、
#3. 取資料：.get()，如果找不到會回傳N/A
#4. 用for loop走訪dict：.items
#for key, value in student.items():

#練習 1：dict（01_dict.py）先建立：
#student = {"name": "Wendy", "age": 28, "scores": [85, 92, 78]}
# 印出 name，再用 student["email"] = "..." 新增一個欄位。
# 用 .get("phone", "N/A") 讀取不存在的 key，並比較直接用 student["phone"] 會發生什麼事。
# 用 for key, value in student.items() 印出所有欄位。
# 建立 grades = {"Amy": 85, "Bob": 72, "Cathy": 91}，找出分數最高的人名（先用迴圈寫）。
# 用 for 迴圈建立一個新 dict，key 是人名、value 是 get_grade 的結果，例如 {"Amy": "B", ...}。

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

student = {"name":"Wendy", "age":28, "score":[85,92,78]}
print("學生姓名：",student["name"])

student["email"] = "wendy@gmail.com"
print("新增email後的student:",student)


phone_number = student.get("phone","N/A")
print("用.get找號碼：", phone_number)

print("\n"+"="*40+"\n")

print("---所有欄位資料---")
for key, value in student.items():
    print(f"{key}:{value}")

print("\n"+"="*40+"\n")

grades = {"Amy":85, "Bob":72, "Cathy":91}
top_studnet = None
max_score = 0

for name, score in grades.items(): #key:name(人名)，第二個值（score)
    if score>max_score:
        max_score = score
        top_studnet = name

print(f"最高分的人是：{top_studnet}({max_score}分)")

print("\n"+"="*40+"\n")
student_grades = {}
for name, score in grades.items():
    student_grades[name] = get_grade(score)

print("原始分數dict:",grades)
print("轉換後的等第dict:", student_grades)