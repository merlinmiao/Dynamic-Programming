#!/usr/bin/python
# -*- coding: utf-8 -*-

#递归法，时间复杂度太大
#方法的时间复杂度是O(2^N)。

def Gold(V,P,W,N):
	if N<=1 and W<P[0]:
		return 0
	if N==1 and W>=P[0]:
		return V[0]
	if N>1: 
		if W<P[N-1]:
			return Gold(V,P,W,N-1)
		if W>=P[N-1]:
			return max(Gold(V,P,W,N-1),Gold(V,P,W-P[N-1],N-1)+V[N-1])


if __name__ == "__main__":
	V=[400,500,200,300,350]
	P=[5,5,3,4,3]
	myList = [([0] * 10) for i in range(5)]
	for N in range(1,6):
		for W in range(1,11):
			myList[N-1][W-1]=Gold(V,P,W,N)
	print myList

