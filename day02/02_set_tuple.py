#把 [1, 2, 2, 3, 3, 3] 轉成 set，觀察結果，並說明 set 的用途。
# a = {1, 2, 3, 4}、b = {3, 4, 5, 6}，分別印出交集、聯集、差集。
# 寫 has_duplicate(items)：list 中有重複元素回傳 True，否則 False（用 set 解）
# 建立 tuple point = (3, 4)，嘗試修改它，看看錯誤訊息，並記下 list 和 tuple 的差別。

my_list = [1,2,2,3,3,3]
my_set = set(my_list)

print("原始list:",my_list)
print("轉成set後：",my_set)

#[set]:自動去重、無序性、極速尋找

print("\n" + "="*40 + "\n")

a = {1,2,3,4}
b = {3,4,5,6}

intersection = a&b
print("交集：",intersection)

union = a|b
print("聯集：",union)

#差集：在a裡面但不在b裡面的元素
difference = a-b
print("差集：",difference)

def has_duplicate(items):
    return len(set(items)) != len(items)

num1 = [1,2,3,4,5]
num2 = [1,2,2,3,4]
print(f"{num1}有重複嗎？", has_duplicate(num1))
print(f"{num2}有重複嗎？", has_duplicate(num2))

point = (3,4)
print("原本的poit:", point)

#list：[]->可改變內容
#tuple：（）->建立後就鎖死，不能更改內容
# try...expect：防呆機制（攔截錯誤、回報細節）

try:
    point[0] = 10
except TypeError as e:  
    print("嘗試修改point[0]得到的錯誤訊息")
    print("TypeError:",e)

#TypeError:錯誤的種類（例如型別錯誤）
#as e：給錯誤訊息取暱稱（取名叫e, 也可以改名叫err)

# 【List vs Tuple 差別整理】
# 1. 語法符號：List 使用中括號 `[]`，Tuple 使用圓括號 `()`。
# 2. 可變性（Mutability）：
#    - List 是「可變的 (Mutable)」，可以隨時新增、刪除、修改元素。
#    - Tuple 是「不可變的 (Immutable)」，一旦建立就無法修改任何內容。
# 3. 使用場景：
#    - List：適合放「同性質且會動態增減」的資料（如：學生成績清單）。
#    - Tuple：適合放「結構固定、不希望被意外修改」的資料（如：GPS 座標 (lat, lon)、顏色 RGB 值 (255, 0, 0)）。