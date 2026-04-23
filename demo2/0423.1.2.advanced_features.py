# 列表生成式

print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = []
for x in range(1, 11):
    L.append(x * x)
print(L) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [x * x for x in range(1, 11)]
print(a) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 筛选出仅偶数的平方
b = [x * x for x in range(1, 11) if x % 2 == 0]
print(b) # [4, 16, 36, 64, 100]

# 使用两层循环，可以生成全排列
c = [m + n for m in 'ABC' for n in 'XYZ']
print(c) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os # 导入os模块
d = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(d)

e = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in e.items():
    print(k, '=', v) # x = A y = B z = C 

print([k + '=' + v for k, v in e.items()]) # ['x=A', 'y=B', 'z=C']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L]) # ['hello', 'world', 'ibm', 'apple']

# 不能在最后的if加上else, 因为跟在for后面的if是一个筛选条件，不能带else
[x if x % 2 == 0 else -x for x in range(1, 10)] # [-1, 2, -3, 4, -5, 6, -7, 8, -9]

# 练习
x = 'abc'
y = 123
isinstance(x, str) # True
isinstance(y, str) # False


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试
print(L2) # ['hello', 'world', 'apple']
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')