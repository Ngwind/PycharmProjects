"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
import time
t1 = time.time()
num = range(0, 20000, 2)
t2 = time.time()
print(t2-t1)
target = 16021
nums = []
t3 = time.time()
for n in num:
    nums.append(n)
nums.append(1)
t4 = time.time()
print(t4-t3)
dict_nums = {}
for i in range(len(nums)):
    dict_nums[nums[i]] = i

for j in range(len(nums)):
    complement = target - nums[j]
    if dict_nums.get(complement) is not None and dict_nums.get(complement) != j:
        print([j, dict_nums.get(complement)])


