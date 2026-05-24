
# 使用场景：
#   while循环： ①无限循环， ②未知循环次数
#   for循环：一般使用在已知循环次数




# 打印1~100的每一个数
'''
i = 1
while i<= 100:
    print(i)
    i += 1
'''

'''
for i in range(1, 101):
    print(i)
'''

# for-in循环：
#  每次循环，i会自动等于右边range中的每一个数

# 求1～100的和
'''
s = 0
for i in range(1, 101):
    s += i
print(s)
'''


# for循环使用场景
# 1.和range结合
#   比如：循环1~10，找到能被3整除的数
'''
for i in range(1, 11):
    if i % 3 == 0:
        print(i)
'''

# 2.和列表结合
# 列表的基本操作
#  元素：列表中的每一个值
nums = [2, 3, 6, 7]
print(f'数组最后一个元素是：{nums[-1]}') # 7 获取倒数第一个元素
print(f'数组长度是：{len(nums)}') # 4
# 直接遍历
for n in nums:
    print(n, end=' ')
print()

# 索引
for i in range(len(nums)):
    print(nums[i], end=' ')
print()

# enumerate 枚举
for i,n in enumerate(nums):
    print(f'索引：{i}，数值：{n}')


# 还可以使用for的有：
#    range()
#    list: [1,2,3]
#    dict: {'name': 'ikun', 'age': 20}
#    tuple: (1,2,3)
#    set: {1,2,3}
#    str: "hello"



