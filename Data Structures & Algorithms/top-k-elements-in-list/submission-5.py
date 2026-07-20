class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # given an array nums
        # return the int k top frequent nums

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        sorted_num = sorted(count, key=count.get, reverse=True)

        return sorted_num[:k]

        