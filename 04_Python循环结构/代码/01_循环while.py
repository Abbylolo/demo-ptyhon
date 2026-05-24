''' '''

# 循环结构：
#    while循环
#    for-in循环

# 循环打印10次100
'''
n = 1 # 循环起始值
while n <= 10: # 循环的条件（结束条件）
    print(100)
    n += 1 # 循环变量
'''


# 死循环：无限循环，循环不会停止
'''
while True:
    print('hello')
'''

#  死循环一般可以和input或time.sleep结合使用
# 需求：不断输入年龄，判断该年龄是否大于30
'''
while True:
    age = int(input('请输入年龄：'))
    if age > 30:
        print('>30')
'''


# 使用场景：
#  1. 无限循环
#  2. 可以是已知循环次数，也可以是未知循环次数



# 需求： 1+2+3+..+100
'''
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
'''






# 练习：计算 10 的阶乘 : 1 * 2 * 3 * ...* 10
#   n的阶乘： 1*2*3*..*n
'''
n = 1
ans = 1
while n <= 10:
    ans *= n
    n += 1
print(ans)
'''


# 练习2：求1~100之间的能被6整数的数的和
'''
s = 0
n = 1
while n <= 100:
    if n % 6 == 0:
        s += n
    n += 1
print(s)
'''


# 练习3：求1~100之间的奇数的个数
cnt = 0
n = 1
while n <= 100:
    cnt += 1
    n += 2

print(cnt)



