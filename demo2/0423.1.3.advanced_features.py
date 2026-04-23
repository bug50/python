# 生成器

# 一边循环一边计算的机制，称为生成器：generator

L = [x * x for x in range(10)]
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
print(g) # <generator object <genexpr> at 0x...>

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

next(g) # 0
next(g) # 1

g = (x * x for x in range(10))
for n in g:
    print(n)

# 斐波拉契数列（Fibonacci）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        # a, b = b, a + b # 这行代码相当于：
        # t = (b, a + b) # t是一个tuple
        # a = t[0] b = t[1]
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6)) # 1 1 2 3 5 done  

for n in fib(6):
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
next(o) # step 1 1
next(o) # step 2 3
next(o) # step 3 5
# next(o) # StopIteration: 生成器没有更多的值可以返回了，会抛出StopIteration异常。

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 练习

# 杨辉三角

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
