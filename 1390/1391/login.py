# def login(username):
#     if username == 'alex':
#         return 'True'
#     else:
#         return 'False'
#
# def detail(user):
#     print(user,'xxxxx')
#
# if __name__ == '__main__':
#     user = input('请输入用户名:')
#
#     result = login(user)
#     if result == 'True':
#         detail(user)
#     else:
#         print('吧吧吧吧吧')

# def foo(name,action='砍柴'):
#     print(name,'去',action)
#
# foo('zhangsan','唱歌')
# foo('lisi','跳舞')
# foo('wangwu','伴奏')
# foo('zhaosi',)

# def show(*arg):
#     for item in arg:
#         print(item)
#
# show('zhangsan','lisi','wangwu','zhaoliu','qiqi')

# def show(**kargs):
#     for item in kargs.items():
#         print(item)
#
# show(a='zhangsan',b='lisi',c='wangwu')

"""
def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

re = foo()
for item in re:
    print(item)


result = 'gt' if 1>3 else 'lt'
print(result)

temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print(temp)
"""
"""
temp = lambda x,y:x+y
print(temp(4,10))
"""

a = []
print(dir())

print(vars())

