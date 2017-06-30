#!/usr/bin/python
# -*- coding: utf-8 -*-

#Range Sum Query - Immutable
#Given nums = [-2, 0, 3, -5, 2, -1]
#
#sumRange(0, 2) -> 1
#sumRange(2, 5) -> -1
#sumRange(0, 5) -> -3
#计算 下标(i->j)之间的数字之和


def sumRange(nums,i,j):
	dp=nums
	for x in xrange(1, len(nums)): 
		dp[x] +=dp[x-1]
	return dp[j] - (dp[i-1] if i > 0 else 0)


if __name__ == "__main__":
#	num = int(raw_input().strip())
	nums = [-2, 0, 3, -5, 2, -1]
	print sumRange(nums,2,5)