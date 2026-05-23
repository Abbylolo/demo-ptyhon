''' '''
# 三大结构
#   1. 顺序结构：代码自上而下执行
#   2. 分支结构
#   3. 循环结构


# if分支结构
# Python语言有强制缩进!!! (因为没有括号 需要根据缩进判断范围，空格数要保持一致)
'''
if True:
    print('Hello')
    print('Hello')
'''

# 单分支
'''
age = int(input('请输入年龄：'))
if age > 18:
    print('恭喜你成年了')

print('end')
'''

# 双分支
'''
age = int(input('请输入年龄：'))
if age > 18:
    print('恭喜你成年了')
else:
    print('您还没成年')
print('end')
'''

# 多分支
#  age范围
#    age<18 : 未成年
#    18~30 : 年轻人
#    30~60 : 中年人
#    age>60 : 老年人
'''
age = int(input('请输入年龄：'))
if age < 18:
    print('未成年')
elif age <= 30:
    print('年轻人')
elif age <= 60:
    print('中年人')
else:
    print('老年人')
print('end')
'''




# 练习：
#    输入年龄age，要求输入0~12岁之间
#    0~3 : 婴儿
#    3~6 ： 幼儿
#    6~12 ：儿童
'''
age = int(input('请输入年龄age：'))
role = ''
if 0 <= age <= 3:
    role = '婴儿'
elif age <= 6:
    role = '幼儿'
elif age < 12:
    role = '儿童'
else:
    role = '不符合0～12岁'
print(role)
'''


# 练习2：
#    输入性别sex,判断sex
#    如果sex=='男'：输出马云
#    如果sex=='女'：输出刘亦菲
#    否则：输出泰国人
'''
sex = input('请输入性别（男/女）：')
if sex == '男':
    print('马云')
elif sex == '女':
    print('刘亦菲')
'''


# if嵌套
#   可以在if语句中 再写if
# 比如：有一个女孩，她母亲要给他介绍对象，女孩有几个要求：
#   1.年龄<=30
#   2.身高>=1.75m
#   3.年薪>=20w
'''
age = int(input('年龄多大了？'))
if age <= 30:
    height = float(input('身高呢？'))
    if height >= 1.75:
        salary = float(input('收入呢？'))
        if salary >= 20:
            print('符合那就见面')
        else:
            print('身高不够')
    else:
        print('身高不够')
else:
    print('年龄太大了')
'''

# if 条件
# bool值隐式判断
'''
if 10:
    print(10)
'''


# 扩展
# 输入2个数，得到较大的数
'''
a = 12
b = 20
if a > b:
    print(a)
else:
    print(b)

# 一行来表示：if-else !!!
c = a if a > b else b
print(c)
'''


# 练习：
#   input("请说出你的心里话(喜欢/不喜欢):")
#   如果喜欢，输出：那就在一起
#   如果不喜欢，输出：那就拜拜
'''
like = input('请说出你的心里话(喜欢/不喜欢):')
print('那就在一起' if like == '喜欢' else '那就拜拜')
'''

# 练习：
# 输入一个成绩score,判断这个成绩属于哪个等级
#    score >= 90: A
#    70<= score <90: B
#    60<= score <70: C
#    score < 60 : D
score = int(input('请输入成绩:'))
if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')

