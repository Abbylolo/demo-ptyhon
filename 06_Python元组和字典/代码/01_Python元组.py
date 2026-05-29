
# 元组 tuple
#    元组就是不可变的列表（不能修改）

# 元组的基本操作
# 1. 创建元组
t = (3) # 3 int 优先识别运算符的括号
t = (3,) # 3 tuple 表示1个元素的元祖，必须添加逗号
t = (3, 4, 5)
print(t, type(t))

# 2. 索引 （同列表）
t = (10, 20, 30)
print(t[0])
print(t[1])
print(t[2])
# print(t[3]) # 报错
print(t[-1]) # 30

# 3. 长度 （同列表）
print(len(t))

# 4.遍历（同列表）
t = (10, 20, 30)
for n in t:
    print(n)

for i in range(len(t)):
    print(i, t[i]) # 索引 元素

for i, n in enumerate(t):
    print(i, n) # 索引 元素

# 5.修改元素 （不可以修改元素）
# t[0] = 666 # 报错：'tuple' object does not support item assignment -- 元组元素不可修改

# 6.切片（同列表）
t = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(t[6:]) # (70, 80, 90)
print(t[:6]) # (10, 20, 30, 40, 50, 60)
print(t[3:7]) # (40, 50, 60, 70)
print(t[2:7:2]) # (30, 50, 70)
print(t[::-1]) # (90, 80, 70, 60, 50, 40, 30, 20, 10)

# 7.加法 （同列表）
print((1, 2, 3) + (4, 5, 6)) # (1, 2, 3, 4, 5, 6)


# 8.乘法（同列表）
print((1, 2, 3) * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 9.成员 （同列表）
if 3 in (1, 2, 3, 4):
    print("3在元组中")


# 元组的功能
# 增 : 不可以
# 删 : 不可以
# 改 : 不可以
# 查 : 索引，切片，循环

# 排序: sorted（了解）
t = (2, 3, 4, 1, 7, 8, 6)
t2 = sorted(t)
print(t2) # [1, 2, 3, 4, 6, 7, 8]


# 转换成list
nums = list(t)
print(nums, type(nums))

# index() : 了解 （同列表）
t = (2, 3, 4, 1, 7, 9, 6)
print(t.index(4)) # 2

# count(): 计数，了解 （同列表）
t = (2, 3, 4, 1, 7, 9, 6)
print(t.count(4))

# 扩展: 快速取值
x, y = 3, 4
x, y = [3, 4]
x, y = (3, 4)
print(f'x:{x},y:{y}')

x, _ = (5, 6)
print(x)

_, y = (5, 6)
print(y)




