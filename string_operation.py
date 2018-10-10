# -*- coding: utf-8 -*-
'''
字符串的一些操作
'''
# 去除前后的空格
line = ' I will always love you\n'
print(line)
# 去除后面的空格
print(line.rstrip())

# 去除前面的空格
print(line.lstrip())

# 字母大小转换
print(line.upper())

# 判断是否全部为字母
print(line.isalpha())

# 判断字符串从尾部开始是否是该字符串
print(line.endswith('you\n'))  # True
print(line.endswith('ou\n'))   # True
print(line.endswith('yu\n'))   # False

# 判断字符串从首部开始是否是该字符串
print(line.startswith(' I'))  # True
print(line.startswith(' I will'))   # True
print(line.startswith('I'))   # False

# 判断某子字符串是否存在
print('you' in line)  # 返回bool型数据
print(line.find('you'))  # 返回子串存在的首个位置下标，20