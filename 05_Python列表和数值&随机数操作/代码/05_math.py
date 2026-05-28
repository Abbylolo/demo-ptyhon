
# 数学操作

#    sum(): 求和
#    max()：最大值
#    min(): 最小值
#    round(): 四舍五入
#    abs(): 绝对值
#    pow(): 次方  (了解)
print(sum([1, 2, 3, 4]))
print(sum(range(1, 101)))

print(max([1, 3, 4, 6]))
# print(max(1, 3, 4, 6))

print(min([1, 3, -3, 9]))

print(round(3.21213213)) # 3
print(round(3.21213213, 2)) # 3.21

print(abs(-3)) # 3

print(pow(2, 3), 2 ** 3)

# math: 数学
import math

print(math.e)
print(math.pi)
print(math.inf)
print(-math.inf)
print(math.sqrt(81), 81 ** 0.5) # 开平方根
print(math.factorial(5)) # 5的阶乘 5!=1*2*3*4*5 = 120

print(math.ceil(3.14)) # 向上取整 4
print(math.floor(3.14)) # 向下取整 3

print(math.log(math.e)) # 自然对数 loge(e) = ln(e) = 1 底数和真数一样，则对数的值为1
print(math.log10(100)) # 2
print(math.log2(2)) # 1

print(math.sin(math.pi))


