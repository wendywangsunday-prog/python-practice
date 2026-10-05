empty_list = []
scores = [85,92,78,90,66]
print(scores[0])
print(scores[-1])

scores.append(78)
scores.remove(66)
total = 0
for a in scores:
    print(a)
    total += a

avg = total/len(scores)
print(f"總分：{total}")
print(f"平均：{avg}")

highest = scores[0]
for a in scores:
    if a > highest:
        highest = a

print(f"最高分：{highest}")

max_score = max(scores)
print(f"[max()函數]最高分是：{max_score}")