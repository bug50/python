# 迭代

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple
# 这种遍历我们称为迭代（Iteration）。

# 在Python中，迭代是通过for ... in来完成的

d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k) # a b c

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样

for ch in 'ABC':
    print(ch) # A B C

# 判断一个对象是可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable)) # True
print(isinstance([1,2,3], Iterable)) # list是否可迭代
print(isinstance(123, Iterable)) # False

# 下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value) # 0 A 1 B 2 C

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y) # 1 1 2 4 3 9

# 练习

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')