# -*- coding: utf-8 -*-
import sys
import math

print('Hello')
print('IDE')
print('Here I am')
print('--------------')
print('Who do you think I am?')
input('输入任意字符：')
print('Oh,yes!')
print('---------------------')

print(sys.path)

print('---------------------')


def foo(x):
    """
    docString
    foo函数用来计算平方根
    作者：Pythoner
    参数：待求平方根的整数
    返回值：平方根或None
    """
    if x >= 0:
        return math.sqrt(x)
    else:
        print(foo.__doc__)
        return None


# __ 双下划线是忽略符，例如：__ = 5
# __doc__ python语言提供的内建(builtin)的隶属于函数的植入变量
print('')
iii = int(input('请输入一个整数：'))
sqrtiii = foo(iii)
print(foo.__doc__)
print(sqrtiii)


def add(num1, num2):
    """
    加法运算
    """
    return num1 + num2


aaa = int(input('请输入第一个数：'))
bbb = int(input('请输入第二个数：'))
ccc = add(aaa, bbb)
print("结果是：%d" % ccc)

# 匿名函数书写方法
map(lambda x: x * x, [y for y in range(10)])
