
# Python数据类型:
#  int, float, str, bool, NoneType,
#  list, tuple, dict, set(了解), bytes

# list列表 : Array数组
# 为什么要使用列表：
# 举例：如果我们表示汽车品牌用变量保存单个值
a = "BYD"
b = "五菱宏光"
c = "小米"
d = "蔚来"
e = "法拉利"
f = "兰博基尼"
g = "路虎"

# 如果要你表示300个品牌, 变量就太多了，这时我们可以使用列表来表示：
cars = ["BYD", "五菱宏光", "小米", "蔚来", "蔚来", "法拉利", "兰博基尼", "路虎"]



# 列表的基本功能
# 1.列表定义
nums = [10, 20, 30, 40, 50] # 不推荐元素类型不统一

# 2.索引,下标
#   从0开始
print(nums[0])
# print(nums[5]) # 索引超出长度报错 IndexError: list index out of range
print(nums[-1]) # 倒数第一个

# 3.长度,元素个数
print(len(nums))

# 4.遍历,循环
for i in range(len(nums)): # 索引
    print(i, nums[i])

for n in nums: # 元素
    print(n)

for i,n in enumerate(nums): # 枚举索引和元素
    print(i, n)

# 5.修改列表
nums = [1, 2, 3]
nums[0] = 66
print(nums)

# 6.切片 (很重要) : 不会修改原列表
#    list[start : stop : step] : [start, stop)
#  和range(start, stop, step)类似  [start, stop)
age = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(age[:5]) # 取索引 [0,5)
print(age[5:]) # 从索引5开始到最后
print(age[2:5]) # 取索引 [2,5)
print(age[2:8:2]) # 步长为2 [30, 50, 70]
# print(age[7:1:-1]) # [80, 70, 60, 50, 40, 30]
print(age[::-1]) # 数组倒序

# 7. 合并 +  (了解)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # 数组合并 [1, 2, 3, 4, 5, 6]

# 8. 重复 * (了解)
print(a * 3) # 重复拼接

# 9. 成员 in (掌握)
if 3 in a:
    print('3 在列表a中')
if 4 not in a:
    print('4 不在列表a中')

# 需求: 列表去重 (掌握)
nums = [1, 2, 3, 3, 5, 5, 5, 6]
nums2 = []
for n in nums:
    if n not in nums2:
        nums2.append(n)
print(nums2)

# 10.删除元素 del (了解)
nums = [10, 20, 30]
# del nums[0] # [20, 30]
del nums[:2] # [30]
print(nums)

