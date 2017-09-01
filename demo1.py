# -*- coding: utf-8 -*-
print('Hello World')

for i in range(0, 100):
    i = i + 1
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

a = input("请输入：")
print(a)
