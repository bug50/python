# 使用dict和set

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d)

d['Jack'] = 90
print(d)
d['Jack'] = 88
print(d)

# d['Thomas'] # KeyError: 'Thomas'

'Thomas' in d  # False

print(d.get('Thomas'))  # None
print(d.get('Thomas', -1))  # -1

d.pop('Bob')
print(d)

# dict是用空间来换取时间的一种方法，通过key快速查找value

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以在set中没有重复的key。

s = {1, 2, 3}
print(s)

s = set([1, 2, 3])
print(s)

s = {1, 2, 3, 3, 3}
print(s)

s.add(4)
s.add(4)
print(s)

s.remove(4)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # 交集
print(s1 | s2)  # 并集
print(s1 ^ s2)  # 不同时存在的元素

# 再议不可变对象
# str是不变对象，而list是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
a = a.replace('a', 'A')
print(a)
