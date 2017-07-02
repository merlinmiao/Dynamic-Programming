#!/usr/bin/python
# -*- coding: utf-8 -*-

#Maximum Subarray
#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
#For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
#the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#子序列中 和最大的序列

def maxSubArray(nums,N):
	dp=[0]*N
	dp[0]=nums[0]
	MAX = dp[0]
	for i in xrange(1, N): 
		dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
		MAX = max(MAX, dp[i]);
	return MAX


if __name__ == "__main__":
#	num = int(raw_input().strip())
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print maxSubArray(nums,len(nums))