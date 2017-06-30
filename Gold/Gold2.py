#!/usr/bin/python
# -*- coding: utf-8 -*-

#动态规划法
#
#结果中的数组下标和人对应
#第0人产生的价值就是result[0]
#第1人产生的价值就是result[1]

def Gold(V,P,W,N):
#	先求第一座矿的价值
	value_kuang1=[]
	results=[]
	for i in range(W+1):
		if i<P[0]:
			value_kuang1.append(0)
		else:
			value_kuang1.append(V[0])
	print 'value_kuang1',value_kuang1
#	后面的矿由第一座矿得出
	for i in range(1,N):
		result = []
		for j in range(W+1):
			if j<P[i]:
				result.append(value_kuang1[j])
			else:
				F=max(value_kuang1[j],value_kuang1[j-P[i]]+V[i])
				result.append(F)
		value_kuang1=result
		print 'value_kuang%d'%(i+1),value_kuang1
		if i==4:
			results=result
			break
	return results


if __name__ == "__main__":
	V=[400,500,200,300,350]
	P=[5,5,3,4,3]
	W=10
	N=5
	result=Gold(V,P,W,N)
	print 'result',result

