
# 逻辑运算符
#   and与(且)  or或者  not非（取反）

# and: 并且
#   2边都为True则为True，只要有一个是False 则为False
# print(True and True)
# print(True and False)
# print(False and False)

# or：或者
#   2边都为False则为False, 只要有一个是True则为True
# print(True or True)
# print(True or False)
# print(False or False)

# not 非，取反
# print(not True) # False

# 不同数据类型 隐式bool值 判断
#   数字类型： 0是假，其他为真
#   字符串类型： 空字符串''为假，其他为真
#   bool类型： False为假，True为真
#   NoneType类型: None是假
#   list类型：空列表[]是假，其他为真
#   tuple元组： 空元组()为假,其他为真
#   dict字典：空字典{}为假，其他为真
# print(bool(0))
# print(bool(''))
# print(bool(None))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool('0')) # True



# 扩展: and和or的短路运算

# and:
#  从左往右依次判断每一个数，只要有一个是False（bool值隐式判断） 则返回该数
print(f'0 and 5 => {0 and 5}') # 0
print(f'3 and 5 => {3 and 5}') # 5
print(f'3 and 0 and print(50) => {3 and 0 and print(50)}') # 0 到0的时候就短路了，不执行后面的print(50)
print('=========')
print(f'3 and print(50) and 0 => {3 and print(50) and 0}') # print(50)函数的返回值是None


# or:
#  从左往右依次判断每一个数，只要有一个是True（bool值隐式判断） 则返回该数
print('=========')
print(f'0 or 5 => {0 or 5}') # 5
print(f'3 or 5 => {3 or 5}') # 3
print('=========')
print(f'0 or print(500) or 10 => {0 or print(500) or 10}')
print('=========')
print(f'0 or 10 or print(500) => {0 or 10 or print(500)}')
print('=========')


# 练习：请直接写出答案（先不要运行）
x = True and 9 # 9
y = False or True or 8 # True = 1
z = x * 3 + y * 2 # 29
print(x, y, z)  #





