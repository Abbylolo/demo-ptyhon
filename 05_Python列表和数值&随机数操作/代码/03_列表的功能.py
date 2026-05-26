
# 列表的功能：对列表中元素操作
#    增删改查

# 增加: 添加元素
#    append(n) : 在列表的末尾追加元素
#    insert(i, n) : 在下标i的位置插入元素n
#    extend(iterable) : 在列表末尾添加多个元素
#           iterable:列表/元组/字符串/字典/集合
# 注意append和extend区别
nums = [1, 2, 3]

nums.append(4)
print(nums) # [1, 2, 3, 4]

nums.insert(0, 6)
print(nums) # [6, 1, 2, 3, 4]

nums.extend([7, 8])
print(nums) # [6, 1, 2, 3, 4, 7, 8]

# append 和 extend 区别
nums = [1, 3, 5]
# nums.append([7, 8]) # 当成一个元素 [1, 3, 5, [7, 8]]
nums.extend([7, 8]) # 拆分加入 [1, 3, 5, 7, 8]
nums.extend('acf') # [1, 3, 5, 7, 8, 'a', 'c', 'f']
print(nums)


# 删除:
#    pop(i) : 弹出(删除并返回)下标i对应的元素, 默认删除最后一个元素
#    remove(n) : 删除指定元素n
#    clear() : 清空列表
nums = [10, 20, 30, 40, 50]
a = nums.pop(2)
print(nums, a)

nums = [2, 3, 4, 5, 3, 5]
nums.remove(3) # 只会删除从左到右第一个匹配的元素 n
print(nums)


# count(): 计数,统计列表中元素出现的次数
# 配合使用删除所有某个元素
nums = [2, 3, 4, 5, 3, 5]
while nums.count(3):
    nums.remove(3)
print(nums)

# clear() : 了解


# 改: 修改元素
nums = [2, 3, 4, 5, 3, 5]
nums.clear()
print(nums)

# 查：修改元素
nums = [1, 2, 3]
nums[1] = 33
print(nums)

# 查: 查询
#  索引: nums[1]
#  切片: nums[2:4]
#  循环: for n in nums:
#       for i in range():
#       for i,n in enumerate(nums):


# index(n) : 获取元素n第一次出现的下标,如果元素不存在则报错
nums = [2, 3, 3, 3, 4, 4, 5]
print(nums.index(3))
# print(nums.index(30)) # 需先判断元素是否存在，否则报错 30 is not in list
if 30 in nums:
    print(nums.index(30))
else:
    print('元素不存在')
print(nums.index(3, 0, 2))

# 排序
#   sort() : 默认升序排列, 直接修改原列表
##     sorted(): 默认升序排列, 不改变原列表 (了解)
#   reverse() : 倒序,逆序, 直接修改原列表
##     reversed() : 倒序,逆序, 不改变原列表 (了解)
nums = [2, 1, 5, 6, 1, 3]
# nums.sort() # [1, 1, 2, 3, 5, 6]
# nums.sort(reverse=True) # [6, 5, 3, 2, 1, 1]
# nums.reverse() # 倒置 [3, 1, 6, 5, 1, 2] # 修改原列表
# print(nums[::-1]) # [3, 1, 6, 5, 1, 2] # 不会修改原列表

# sorted() 了解
nums2 = sorted(nums, reverse=True)
print(nums) # [2, 1, 5, 6, 1, 3]
print(nums2) # [6, 5, 3, 2, 1, 1]

# reversed() 了解
nums = [2, 1, 5, 6, 1, 3]
nums2 = reversed(nums)
print(nums) # [6, 5, 3, 2, 1, 1]
print(nums2) # <list_reverseiterator object at 0x10b82fcd0>
print(list(nums2)) # 倒置 [3, 1, 6, 5, 1, 2]


# 复制数组
nums = [1, 2, 3]
nums2 = nums
nums[0] = 9
nums2[1] = 8
print(nums) # [9, 8, 3]
print(nums2) # [9, 8, 3]

# copy(): 复制,拷贝
# 浅拷贝（Shallow Copy）
nums = [1, 2, 3]
nums2 = nums.copy()
nums[0] = 9
print(nums) # [9, 2, 3]
print(nums2) # [1, 2, 3]


