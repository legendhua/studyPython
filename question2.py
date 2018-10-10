# -*- coding: utf-8 -*-
'''
好未来笔试第二题
'''
l, r = [int(s) for s in input().split()]


def decide(n):
    if n>=0 and n<=9:
        return True,1
    s = str(n)
    if s[0]==s[-1]:
        return True,10-int(s[0])
    else:
        return False,1


def main(l, r):
    len_l = len(str(l))
    len_r = len(str(r))
    num1 = 9 * (len_r-1)
    num2 = fun(1,l)
    num3 = fun(int('1'+'0'*(len_r-1)),r+1)
    print(num1-num2+num3)

def fun(start, end):
    count = 0
    while start < end:
        flag, add = decide(start)
        if flag:
            count += 1
        start += add
    return count

main(l,r)