# 函数的参数

# 位置参数

def power(x):
    return x * x

print(power(5))
print(power(15))

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 2))
print(power(5, 3))

# 默认参数

# 一是必选参数在前，默认参数在后
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 3))

def enroll(name, gender, age = 6, city = 'Beijing'):
    print(f'name: {name}')
    print(f'gender: {gender}')
    print(f'age: {age}')
    print(f'city: {city}')

enroll('Sarah', 'F')
enroll('Bob', 'M', 79, 'Guangzhou')
enroll('Bob', 'M', 7, city = 'Shanghai')

def add_end(L = []):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())

def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())
# 可变参数

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3]))
print(calc([1, 2, 3, 4]))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2, 3))
print(calc(1, 2, 3, 4))
print(calc())

nums = [1, 2, 3]
print(calc(*nums))
print(calc(*[1, 2, 3]))

# 关键字参数

def person(name, age, **kw):
    print(f'name: {name}')
    print(f'age: {age}')
    print(f'other: {kw}')

print(person('Bob', 25, city='Beijing'))
print(person('Adam', 45, gender='M', job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
print(person('Jack', 245, **extra))

# 命名关键字参数

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print(f'name: {name}, age: {age}, other: {kw}')

print(person('Jack', 124, city='Beijing', addr='Chaoyang', zipcode=123456))

def person(name, age, *, city, job):
    print(name, age, city, job)

print(person('Jack', 124, city='Beijing', job='Engineer'))

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 缺少参数名city和job
# 后两个参数传给*args，但缺少命名关键字参数导致报错
# print(person('Jack', 124, 'Beijing', 'Engineer'))

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

print(person('Jack', 124, job='Engineer'))

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

# 参数组合

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))

# 练习

def mul(*args):
    if len(args) == 0:
        raise TypeError('mul()至少要有一个参数')
    product = 1
    for n in args:
        product = product * n
    return product

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。