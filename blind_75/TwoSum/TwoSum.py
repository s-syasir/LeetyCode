from typing import List


def main():
    print("Hello World!")
    solu = Solution
    testInput = [1, 3, 2, 0]
    value = solu.twoSum(solu, testInput, 2)
    print(value)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if (not nums[i] in store):
                store[nums[i]] = i
            diff = target - nums[i]
            if (diff in store and store[diff] != i):
                return [store[diff], i]
        return [-1, -1]


if __name__ == "__main__":
    main()
