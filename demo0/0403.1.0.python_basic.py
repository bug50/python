# print absolute value of an integer
a = 100
# 当语句以冒号:结尾时，缩进的语句视为代码块
if a >= 0:
    # 始终坚持使用4个空格的缩进
    print(a)
else:
    print(-a)

# Python程序是大小写敏感的

# 数据类型和变量

print('I\'m ok.')

# \n表示换行
print('I\'m learning\nPython.')

print('\\\n\\')

# \t表示制表符
print('\\\t\\')

# r表示原始字符串，不进行转义
print(r'\\\t\\')

# '''表示多行字符串
print('''lin1
lin2
lin3''')

print(r'''hello,\n
world!''')

print(True)
print(False)
print(3 > 2)
print(3 < 2)
print(True and False)
print(True or False)
print(not True)
print(not False)

age = 18
if age >= 18:
    print('you are an adult.')
else:
    print('you are a minor.')

t_007 = 'T007'

b = 123
print(b)
b = 'abc'
print(b)

x = 100
x = x + 100
print(x)


print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)

# 练习
n = 123
f = 456.789
s1 = 'Hello, world!'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）