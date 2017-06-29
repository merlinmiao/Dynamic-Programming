# -*- coding: utf-8 -*-

#走楼梯问题
def climb(n):
    if n<1:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    a=1
    b=2
    temp=0
    for i in range(3,n+1):
        temp=a+b
        a=b
        b=temp
    return temp


if __name__ == "__main__":
    num = int(raw_input().strip())
    print climb(num)
