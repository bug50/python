# 递归函数

# 阶乘函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(1))
print(fact(5))
print(fact(100))
# print(fact(1000)) # 栈溢出

# 解决递归调用栈溢出的方法是通过尾递归优化

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# print(fact(1000)) # 栈溢出

# Python解释器没有做优化
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

# 练习

def move(n, a, b, c):
    if n == 1:
        print(f'{a} --> {c}')
    else:
        move(n - 1, a, c, b)
        print(f'{a} --> {c}')
        move(n - 1, b, a, c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')