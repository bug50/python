# 调用函数

print(abs(-1))  # abs()函数求绝对值

# print(abs(1,20))  # TypeError: abs() takes exactly one argument (2 given)

# print(abs('a'))  # TypeError: bad operand type for abs(): 'str'

print(max(1, 2, 3))  # max()函数可以接收任意多个参数，并返回最大的那个

# 数据类型转换

print(int('123'))  # 将字符串转换为整数
print(int(12.34))  # 将浮点数转换为整数，丢掉小数部分
print(float('123.45'))  # 将字符串转换为浮点数
print(str(123))  # 将整数转换为字符串
print(bool(1))  # 将0转换为False，非0的数值都转换为True
print(bool(''))  # 将空字符串转换为False，非空字符串转换为True

a = abs
print(a(-1))

# 练习

n1 = 255
n2 = 1000

print(hex(n1))  # hex()函数把一个整数转换成十六进制表示的字符串，前面带0x
print(hex(n2))  # hex()函数把一个整数转换成十六进制表示的字符串，前面带0x