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

# 格式化操作
x = 1234
# 第一个为默认正常输出，第二个为6位左对齐输出，第三个为6位右对齐输出，第四个为6位右对齐左补0
res = "the result is:...%d...%-6d...%6d...%06d"%(x,x,x,x)
print(res)

y = 1.23456
# 第一个为6位左对齐3位小数，第二个为6位右对齐左补03位小数
res = "the result is:...%-6.3f...%06.3f..."%(y,y)
print(res)

# 基于字典的字符串格式化
reply = '''
Greeting...
Hello,%(name)s,
my age is %(age)d.
'''
values = {'name':'Bob','age':30}
print(reply % values)

# 通过位置或者关键字来进行格式化字符串
template = '{0}, {1} and {2}'   # by position
print(template.format('spam','ham','eggs'))

template = '{motto}, {pork} and {food}'  # by keyword
print(template.format(motto='spam',pork='ham',food='eggs'))

template = '{motto}, {0} and {food}'  # by both
print(template.format('ham',motto='spam', food = 'eggs'))
