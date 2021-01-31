class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        first_part = nums[0]
        second_part_target = target - first_part
        second_part = None
        nums_for_indexes = nums.copy()
        while second_part != second_part_target:
            nums.pop(0)
            for i in nums:
                if i == second_part_target:
                    second_part = second_part_target
                    first_part_index = nums_for_indexes.index(first_part)
                    nums_for_indexes[first_part_index] = 'x'
                    second_part_index = nums_for_indexes.index(second_part)
                    return [first_part_index, second_part_index]
                elif i == nums[-1]:
                    first_part = nums[0]
                    second_part_target = target - first_part

        # h = {}
        # for i, num in enumerate(nums):
        #     n = target - num
        #     if n not in h:
        #         h[num] = i
        #     else:
        #         return [h[n], i]


x1n = [2, 7, 11, 15, 8, 9, 16, 13]
x1t = 20
x2n = [3, 2, 4]
x2t = 6
x3n = [3, 3]
x3t = 6
s = Solution()

print(s.twoSum(x1n, x1t))
print(s.twoSum(x2n, x2t))
print(s.twoSum(x3n, x3t))
