# 循环

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(list(range(5)))

sum = 0
# 生成0-100的整数序列
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 练习
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(f'Hello, {name}!')

# break

n = 1
while n <= 10:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# continue

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)