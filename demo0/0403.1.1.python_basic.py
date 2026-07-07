# 字符串和编码

print('包含中文的str')

# ord()函数获取字符的整数表示
print(ord('A'))
print(ord('中'))

# chr()函数将整数转换为对应的字符
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

# 以Unicode表示的str通过encode()方法可以编码为指定的byte
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 中文编码的范围超过了ASCII编码的范围，Python会报错
# print('中文'.encode('ascii'))

# 字符串解码
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中包含无法解码的字节，decode()方法会报错
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# len()函数计算的是str的字符数
print(len('中文'))
print(len(b'ABC')) # 3

# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 格式化

# %s表示用字符串替换，%d表示用整数替换，%f表示用浮点数替换，%x表示用十六进制数替换。
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 如果只有一个%?，括号可以省略
print('Hi, %s.' % 'Michael')

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))

# 用%%来表示一个%
print('growth rate: %d %%' % 7)

# format() 用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# f-string 字符串如果包含{xxx}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'圆的半径是{r}，面积是{s:.2f}')

# 练习
ss = 72
sss = 85
rr = (sss - ss) / ss * 100
print(f'小明成绩提升了{sss - ss}分，提升了{rr:.1f}%')