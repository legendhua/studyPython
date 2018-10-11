# -*- coding: utf-8 -*-
'''
列表的一些容易忘记的操作
'''
a = [1,2,3,4]
print(a)
# 列表的扩展
a.extend([5,6,4])
print(a)
# 查询某个数在列表中的第一个索引位置
print(a.index(4))
# 统计某个数在列表中的个数
print(a.count(4))
# 按照切片删除列表中的某些数
del a[0]  # 按照索引删除
del a[3:6]
print(a)
a.append(3)
a.remove(3) # 按照数字删掉第一个
print(a)