def max_end3(nums):
  x = max(nums[0],nums[-1])
  for i in range(len(nums)):
    nums[i] = int(x)
  return nums
