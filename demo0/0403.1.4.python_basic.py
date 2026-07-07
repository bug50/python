# 模式匹配

score = 'A'
if score == 'A':
    print('优秀')
elif score == 'B':
    print('良好')
elif score == 'C':
    print('中等')
elif score == 'D':
    print('及格')
else:
    print('不及格')

score_ = 'B'
# Match 语句需要 Python 3.10 或更高版本
# match score_:
#     case 'A':
#         print('优秀')
#     case 'B':
#         print('良好')
#     case 'C':
#         print('中等')
#     case 'D':
#         print('及格')
#     case _:
#         print('不及格')

# 复杂匹配

age = 15
# match age:
#     # 第一个case x if x < 10表示当age < 10成立时匹配，且赋值给变量x
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')

# 匹配列表

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件: 第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')
