#!/usr/bin/python
# -*- coding: utf-8 -*-

#问题描述：
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

#动态规划思想
#f(0) = nums[0]
#f(1) = max(num[0], num[1])
#f(k) = max( f(k-2) + nums[k], f(k-1) )


def robber(nums,lenth):
	if lenth == 0:
		return 0
	if lenth == 1:
		return nums[0]
	if lenth == 2:
		return max(nums[0], nums[1])
	a=nums[0]
	b=max(nums[0], nums[1])
	temp=0
	for i in range(2,lenth): 
		temp =max( a + nums[i], b )
		a=b
		b=temp
	return temp


if __name__ == "__main__":
#	num = int(raw_input().strip())
	nums = [2, 6, 3, 5, 2, 1]
	lenth=len(nums)
	print robber(nums,lenth)
