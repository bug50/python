# 使用list和tuple

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# 往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 插入元素到指定位置
classmates.insert(1, 'Jack')    
print(classmates)

# 删除list末尾的元素
classmates.pop()
print(classmates)

# 删除指定位置的元素
classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

# tuple 元组，元组一旦创建，就不能修改，元组的元素也不能修改 没有append()，insert()，pop()等方法

t = ('Michael', 'Bob', 'Tracy')
# t[0] = 'Adam' # TypeError: 'tuple' object does not support item assignment
print(t)

t = ()
print(t)

# 按小括号进行计算，计算结果自然是1
t = (1)
print(t)

t = (1,)
print(t)

# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
print(t)

# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob: 
print(L[2][2])
