# -*- coding: utf-8 -*-
'''
转义字符的一些知识，包括抑制转义字符、反斜杠个数的区别
'''
path1 = 'C:\new\text.txt'
print(path1)
print(len(path1))  # 转义字符为一个字符

path2 = r'C:\new\text.txt'  # 通过raw字符串抑制转义字符
print(path2)
print(len(path2))   # 非转义字符

# 字符串中不能以单个反斜杠结尾，且字符串中反斜杠个数为奇数个
# 输出3个反斜杠的解决办法
# print('..\\\') 错误
# print(r'..\\\') 错误
print(r'..\\'+'\\') # 偶数基础上手动增加一个反斜杠
print(r'..\\\\'[:-1]) # 分片解决
print('..\\\\\\') # 双反斜杠