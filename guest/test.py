"""
def transfer():
    ip = '10.3.9.2'
    a = ip.split('.')
    l = []
    for i in a:
        i = bin(int(i))[2:]
        i = i.rjust(8, '0')
        l.append(i)
    s = ''.join(l)
    return s


print(int(transfer(), 2))
"""

import sys

# sys.setrecursionlimit(100000000)

# x = input(">")
# y = input(">>")
# z = input(">>>")

# print((x if (x > y) else y) if ((x if (x > y) else y) > z) else z)

# from functools import reduce
# add = lambda x, y: x * y
# print(add(2, 3))

# ls = [1, 2, 32, 4, 23, 12]
# print(reduce(lambda x, y: x + y, ls))


# def num():
#     return [lambda x: i * x for i in range(4)]
#
#
# print([m(2) for m in num()])


# def foo1(n):
#     def foo2(m):
#         return n + m
#
#     return foo2
#
#
# a = foo1(2)
# print(a(3))


# print('\n'.join(' '.join('%s*%s=%-2s' % (y, x, x * y) for y in range(1, 1 + x)) for x in range(1, 10)))


# print('\n'.join(' '.join('%s*%s=%-2s' % (y, x, y * x) for y in range(1, 1 + x)) for x in range(1, 10)))

# import re
#
# str = "1,2,3,1212,34,343,23"
# ret = re.findall('\d+', str)
#
# res = list(map(int, ret))
# print(res)

# a = list(map(lambda x: x ** 2, range(11)))
# print(a)

# 后进先出
# class Stack():
#     def __init__(self, size):
#         self.size = size
#         self.stack = []
#         self.top = -1
#
#     # 入栈之前检查栈是否已满
#     def push(self, x):
#         if self.isfull():
#             raise Exception("stack is full")
#         else:
#             self.stack.append(x)
#             self.top = self.top + 1
#
#     # 出栈之前检查栈是否为空
#     def pop(self):
#         if self.isempty():
#             raise Exception("stack is empty")
#         else:
#             self.top = self.top - 1
#             self.stack.pop()
#
#     def isfull(self):
#         return self.top + 1 == self.size
#
#     def isempty(self):
#         return self.top - 1 == self.size
#
#     def showStack(self):
#         print(self.stack)
#
#
# s = Stack(10)
# for i in range(6):
#     s.push(i)   # 入栈
# s.showStack()
#
#
# for i in range(2):
#     s.pop()     # 出栈
# s.showStack()

"""
class Stack():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push('h')
    my_stack.push('a')
    print(my_stack.size())
    my_stack.pop()
    print(my_stack.peek())
    my_stack.pop()
    print(my_stack.is_empty())
"""

"""
def fab(max):
    L = []
    n, a, b = 0, 0, 1
    while n < max:
        L.append(b)
        a, b = b, a + b
        n += 1
    return L


print(fab(10))
"""

"""
import math


def binary_search(list1, item):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if list1[mid] == item:
            return mid
        # 左半边
        elif list1[mid] > item:
            high = mid - 1
        # 右半边
        else:
            low = mid + 1
    # 未找到返回-1
    return None


my_list = [x for x in range(1, 100000)]
print(binary_search(my_list, 7))
print(binary_search(my_list, 33452))
"""

# import random
#
# i = 1
# a = random.randint(0, 100)
# b = int(input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
# while a != b:
#     if a > b:
#         print('你第%d输入的数字小于电脑随机数字' % i)
#         b = int(input('请再次输入数字:'))
#     else:
#         print('你第%d输入的数字大于电脑随机数字' % i)
#         b = int(input('请再次输入数字:'))
#     i += 1
# else:
#     print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样' % (i, b))

# class Foo:
#     pass
#
# class Bar(Foo):
#     pass
#
# f1 = Foo()
# print(isinstance(f1,Foo))
# print(issubclass(Bar,Foo))

"""
class Animals(object):
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("Hello, I am %s" % self.name)


class Dog(Animals):
    def greeting(self):
        super().greeting()
        print('wangwangwang...')


dog = Dog('Jim')
dog.greeting()
"""

"""
class BaseClass(object):
    def __init__(self):
        print('enter BaseClass')
        print('leave BaseClass')


class A(BaseClass):
    def __init__(self):
        print('enter A')
        super(A, self).__init__()
        print('leave A')


class B(BaseClass):
    def __init__(self):
        print('enter B')
        super(B, self).__init__()
        print('leave B')


class C(B, A):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')


c = C()
"""

"""
class Foo:
    def __getitem__(self, item):
        print('getitem')
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        print('setitem')

    def __delitem__(self, key):
        self.__dict__.pop(key)
        print('delitem')


f1 = Foo()
print(f1.__dict__)

f1['name'] = 'goodslin'
f1['age'] = 18
print(f1.__dict__)

print(f1.__dict__)

del f1['age']
print(f1.__dict__)
"""

"""
class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        #实例方法
        print('实例方法')

    @classmethod
    def class_func(cls):
        print('类方法')

    @staticmethod
    def static_func():
        print('静态方法')


f = Foo("zibuyu")
f.ord_func()

Foo.class_func()

f.static_func()
Foo.static_func()
"""

# L = []
# # for x in range(1, 6):
# #     for y in range(1, 6):
# #         for z in range(1, 6):
# #             if (x != y) and (x != z) and (y != z):
# #                 L.append("%s%s%s" % (x, y, z))
# # print(L)


# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == 'warn':
#                 print("%s is running" % func.__name__)
#             elif level == 'info':
#                 print("%s is not running" % func.__name__)
#             return func(*args)
#         return wrapper
#
#     return decorator
#
#
# @use_logging(level='warn')
# def foo(name='foo'):
#     print('i am %s' % name)
#
# 
# foo()


"""
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class decorator running')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()
"""


# class Solution(object):
#     nums = [2, 7, 11, 15, 2]
#
#     def twoSum(self, target, nums=nums):
#         for i in range(len(nums)):
#             if (target - nums[i]) in nums:
#                 idx = nums.index(target - nums[i])
#                 if i == idx:
#                     pass
#                 else:
#                     return [i, idx]
#
#
#
# obj = Solution()
# print(obj.twoSum(4))

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums:
                idx = nums.index(target - nums[i])
                if idx != i:
                    return [i, idx]
                else:
                    pass


obj = Solution()
nums = [2, 7, 11, 15]
print(obj.twoSum(nums, 9))
