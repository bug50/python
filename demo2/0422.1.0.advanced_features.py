# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素
# 笨办法
print([L[0], L[1], L[2]])

# 循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

# 切片（Slice）操作符
print(L[0:3])

# 如果第一个索引是0，还可以省略
print(L[:3])  # 省略0

print(L[1:3])  # 从索引1开始取，直到索引3为止，但不包括索引3

print(L[-2:])  # 取倒数两个元素

print(L[-2:-1])  # 取倒数第二个元素

L = list(range(100))
print(L)
print(L[:10])  # 取前10个数，不包括第10个元素
print(L[-10:])  # 取后10个数
print(L[10:20])  # 取第11个到第20个元素

print(L[::5])  # 取所有元素，每5个取一个

print(L[:])  # 复制一个新的列表

# tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])

print('ABCDEFG'[::2])  # 取所有元素，每2个取一个

# 练习

def trim(s):
    if s == '':
        return s
    while s[0] == ' ':
        s = s[1:]
        if s == '':
            return s
    while s[-1] == ' ':
        s = s[:-1]
    return s

# 测试

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')