
# Python
#   不可变类型: int,float,str,tuple,bool,NoneType
#    可变类型: list, set, dict

# 赋值
# 不可变类型 (没有关联)
a = 10
b = a
b = 20
print(f'a:{a}, b:{b}') # a:10, b:20

# 可变类型 (有关联) -- JAVA中叫引用类型
a = [1, 2, 3]
b = a
b[0] = 888
print(f'a:{a}, b:{b}') # a:[888, 2, 3], b:[888, 2, 3]


# 深浅拷贝的可视化视图
#  http://pythontutor.com/live.html#mode=edit

# copy: 浅拷贝/浅复制
a = [1, 2, 3, [2,3]]
b = a.copy()
b[0] = 999
b[3][0] = 88
print(f'a:{a}, b:{b}') # a:[1, 2, 3, [88, 3]], b:[999, 2, 3, [88, 3]]


# deepcopy 深拷贝(针对多维数组)
import copy
a = [1, 2, 3, [2,3]]
b = copy.deepcopy(a)
b[0] = 999
b[3][0] = 88
print(f'a:{a}, b:{b}') # a:[1, 2, 3, [2, 3]], b:[999, 2, 3, [88, 3]]
