students = [
    {"name":"Amy","score":85},
    {"name":"Bob","score":72},
    {"name":"Cathy","score":91},
]
#寫 get_average(students)：回傳全班平均。

def get_average(students):
    total = 0
    for a in students:
        total += a["score"]
    return total/len(students) 

#寫 get_top_student(students)：回傳分數最高的學生 dict。
def get_top_student(students):
    hightest = 0
    hightest_name = None
    for a in students:
        if a["score"]>hightest:
            highest = a["score"]
            hightest_name = a
    return hightest_name


#寫 get_passed(students, passing=60)：回傳及格學生的名字 list。
def get_passed(students, passing=60):
    pass_list = []
    for a in students:
        if a["score"]>=passing:
            pass_list.append(a["name"])
    return pass_list


#寫一個迴圈，印出每個人的 姓名 - 分數 - 等級。
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >=70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

avg_score = get_average(students)
print(f"全班平均分數：{avg_score:.2f}分")

top = get_top_student(students)
print(f"最高分學生：{top}")

print(f"及格的學生：{get_passed(students)}")

for a in students:
    name = a["name"]
    score = a["score"]
    grade = get_grade(score)
    print(f"{name}-{score}分-等級{grade}")