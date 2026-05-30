
# 字符串的基本操作
#  str : 引号包裹的就是字符串 'abc'  "abc" """abc"""

# 1.创建字符串
s = "大大开阔的"
print(s)

# 2.索引
print(s[0])

# 3.长度
print(len(s))

# 4. 循环
for c in s: # 字符
    print(c)

for i in range(len(s)): # 索引
    print(i, s[i])

for i, c in enumerate(s): # 索引，字符
    print(i, c)

# 5.修改字符串: 字符串str是不可变类型
# s[0] = '打' # 报错：'str' object does not support item assignment
s += '的' # s = s + '的' 没改变原字符串，做了字符串拼接重新赋值
print(s)

# 6.切片
s = 'ABCDEF'
print(s[:4]) # ABCD
print(s[4:]) # EF
print(s[2:4]) #CD
print(s[:5:2])
print(s[::-1])

# 7.加法
print('abc' + 'def') # abcdef

# 8.乘法
print('abc' * 3) # abcabcabc

# 9.成员
print('a' in s)

