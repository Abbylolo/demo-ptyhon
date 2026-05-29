
# 字典 dict  dictionary字典

# dict特点：
#   1. 字典的key不能重复 （key 唯一性）
#   2. 字典的key不可以是 可变类型(list,dict,set)，但是建议使用字符串
#   3.  key无序性

# 1.创建
#  key:value ：键值对
d = {'name': '张三丰', 'age': 200, 'age': 2, 1: 5}
# d = {[1, 2]: 5} # 报错：unhashable type: 'list'
# d = {{1, 2}: 5} # 报错：unhashable type: 'set'
print(d)


# 2.索引 : 没有数字索引，但是可以使用key
d = {'name': '张三丰', 'age': 200}
# print(d[0]) # 报错：key不存在 KeyError: 0
print(d['name'])
print(d.get('name1')) # None 找不到不会报错，会返回None
print(d.get('sex', '女')) # 如果找不到sex，则使用默认值“女”

# 3.长度
print(len(d))

# 4.遍历
print(list(d.keys())) # 所有的key ['name', 'age']
print(list(d.values())) # 所有的value ['张三丰', 200]
print(list(d.items())) # 所有的value [('name', '张三丰'), ('age', 200)]
# 方法 1：直接遍历键（推荐）
for key in d:
    print(f'key:{key}, value:{d[key]}')
# 方法 2：遍历键值对（推荐）
for key, val in d.items():
    print(f'法二：key:{key}, value:{val}')

# 不推荐
'''
for key in d.keys():
    print(f'key:{key}, value:{d[key]}')
'''

# 用的少
'''
for val in d.values():
    print(val)
'''


# 5.修改元素
d = {'name': '张三丰', 'age': 200}
d['name'] = '聂风'
print(d)


# 6.切片: 不可以
# dict没有数字索引，而且dict是无序的，所以没有切片


# 7.合并
d1 = {'a': 100}
d2 = {'b': 200}

# print(d1 + d2) # 报错：unsupported operand type(s) for +: 'dict' and 'dict'
d1.update(d2) # 将d2合并到d1里
print(d1, d2)

# 8.重复： 不可以
# print(d1 * 3) # 报错：unsupported operand type(s) for *: 'dict' and 'int'

# 9.成员 (掌握)
if 'name' in d:
    print('name是字典d的key')


# 字典的功能
# 增删改查
#  增，改
d['name'] = 'abby' # 修改：key存在
d['sex'] = '男' # 新增：key不存在
print(d)


# 删：
#  pop(key): 删除key对应的元素 (掌握 )
#  clear() : 清空字典 （了解）
#  popitem() : 删除一个元素 （了解）删除的是字典中最后一个键值对

# d.pop('name')
# d.clear()
d.popitem()
print(d)




