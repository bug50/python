# 条件判断

a = 2
if a >= 18:
    print('your age is', a)
    print('adult')
elif a >= 6:
    print('your age is', a)
    print('teenager')
else:
    print('your age is', a)
    print('kid')

x = 1
# 只要x是非零数值、非空字符串、非空list等，就判断为True
if x:
    print('True')

# 再议input

# input()返回的数据类型是str，str不能直接和整数比较
birth = input('请输入：')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 练习
height = 1.75
weight = 80.5
bmi = weight / (height * height)

if bmi < 18.5:
    print('过轻')
elif bmi < 24:
    print('正常')
elif bmi < 28:
    print('过重')
else:
    print('肥胖')