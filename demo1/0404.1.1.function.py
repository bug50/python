# 定义函数

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    
print(my_abs(-99))

# 如果你已经把my_abs()的函数定义保存为abstest.py文件了
# 那么，可以在该文件的当前目录下启动Python解释器
# 用from abstest import my_abs来导入my_abs()函数
# 注意abstest是文件名（不含.py扩展名）

# from abstest import my_abs
# print(my_abs(-99))

# 空函数

# 定义一个什么事也不做的空函数，可以用pass语句
# 实际上pass可以用来作为占位符
def nop():
    pass

age = 18
if age >= 18:
    pass    # TODO: 还没有想好怎么处理未成年人的情况

# 参数检查

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
# print(my_abs('A'))

# 返回多个值

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    # 函数可以同时返回多个值，但其实就是一个tuple。
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# 练习

import math

def quadratic(a, b, c):
    if a == 0:
        raise TypeError('a不能为0')
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError('无实数解')
    elif delta == 0:
        return -b / (2 * a)
    else:
        return (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)

# 测试
print(quadratic(2, 3, 1))
print(quadratic(1, 2, 1))

if quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败!')
elif quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败!')
else:
    print('测试成功!')