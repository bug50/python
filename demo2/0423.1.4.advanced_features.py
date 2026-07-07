# 迭代器

# 可以直接作用于for循环的对象统称为可迭代对象：Iterable

# 使用isinstance()判断一个对象是否是Iterable对象

from collections import Iterable
print(isinstance('abc', Iterable)) # True
print(isinstance([1, 2, 3], Iterable)) # True
print(isinstance(123, Iterable)) # False
print(isinstance({1, 2, 3}, Iterable)) # True
print(isinstance({'a': 1}, Iterable)) # True
print(isinstance(None, Iterable)) # False

# Iterable变成Iterator可以使用iter()函数
from collections.abc import Iterator
print(isinstance(iter('abc'), Iterable)) # True
print(isinstance(iter([]), Iterator)) # True

# Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算下一个数据
# 而不是直接计算出所有数据

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列

for x in [1, 2, 3, 4, 5]:
    pass

# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
