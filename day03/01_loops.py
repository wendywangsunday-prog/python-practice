#用 names = ["Amy", "Bob", "Cathy"]、scores = [85, 72, 91]：
names = ["Amy" , "Bob" , "Cathy"]
scores = [85,72,91]

#1.用 enumerate(names, start=1) 印出 1. Amy、2. Bob……（列舉）
#for A, B in enumerate(...)->A:編號, B:元素內容

for index, name in enumerate(names, start=1): #不寫1會從0開始







用 zip(names, scores) 印出 Amy: 85 這樣的格式。
用 zip 建立 dict：{"Amy": 85, "Bob": 72, "Cathy": 91}。
用 range(1, 21, 2) 印出 1 到 20 的奇數。
用 break 和 continue 各寫一個小例子，例如找到第一個不及格的分數就停止、跳過負數。