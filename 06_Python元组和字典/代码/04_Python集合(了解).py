
# 集合 set
#   特点: 唯一性(去重), 无序性, 元素不能是可变类型(list,dict,set)

# 1.创建集合
s = {1, 2, 2, 3, 4, 1, (1,2)}
print(s) # {1, 2, 3, 4}

s = {} # 空字典
s = set() # 空集合
print(s, type(s)) # set() <class 'set'>

# 2.不能用索引
# print(s[0]) # 报错：'set' object is not subscriptable

# 3.长度
s = {1, 2, 2, 3, 4, 1} # 4
print(len(s))

# 4.循环
for n in s:
    print(n)

# 5.修改:删除一个,然后再添加新的
# 6.不能用切片
# 7.不能用加法
# 8.不能用乘法
# 9.成员
print(3 in {1, 2, 4, 3})


# 功能(了解）
#  add(): 添加元素
#  pop(): 是删除并返回集合中的任意一个元素
#  clear(): 清空
#  remove(3)  # 删除元素3,如果元素不存在会报错
#  discard(3)  # 删除元素3,如果元素不存在不会报错
s = {1, 2, 3, 99}
# s.add(4)
# s.pop()
# s.clear()
# s.remove(98) # 找不到会报错：KeyError: 98
s.discard(99) # 找不到不报错
print(s)




print('==============')
# 集合关系
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)  # 交集  {3, 4}
print(s1 | s2)  # 并集 {1, 2, 3, 4, 5, 6}
print(s1 - s2)  # 差集（相对补集） {1, 2}, 只存在s1中的元素
print(s1 >= s2)  # 包含关系 True ,表示s1中是否全部包含s2的元素


print('==============')
# 练习：利用集合去重
nums = [1, 3, 3, 2, 2, 2, 4, 5, 4, 5]
print(list(set(nums)))


