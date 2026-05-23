

# Python算术运算符：
#    +  -  *  /  %余数  //（整除:向下取整）   **取幂
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 / 4)
print(10 // 4)
print(-10 // 4)
print(10 ** 4)


# 科学计数法
a = 3.14 * 10**5
b = 3.14e5
print(a, b, sep="...")



# 常见内存单位：
# 1bit = 0 或 1
# 1Byte = 8bit
# 1KB = 1024Byte
# 1MB = 1024KB
# 1GB = 1024MB
# 1TB = 1024GB
# 1PB = 1024TB
# 1EB = 1024PB
# ...

# 练习：从控制台输入一个三位数，取出个位，十位，百位
n = int(input("请输入一个三位数："))
print(n % 10, n // 10 % 10, n // 100)
