from typing import List
# Main. This is where you test the solution class that was generated by calling on it.
def main():
    print("Hello World!")
    solution_obj = Solution
    retVal = solution_obj.majorityElement(solution_obj, [1,2,2,3,4,5,5,5,5,5])
    print(retVal)


# TODO: change the name of the defined method "something" to the problem name
# TODO: Write out the solution for the problem, writing out the class and method
# TODO: ensure the return value and parameters match the problem

# Easy solution: Store the frequency of each number. Return the one that has value > len/2
# Tryhard. Need to do it O(N) with 0 storage. Just figure out on the fly if you : go through the list once. 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxOccurence = 1
        maxOccuringIndex = 0
        maxOccuringVal = nums[0]
        for i in range(0,len(nums)):

        return maxOccuringVal

# If this is the file that is running "__name__ == __main__",
# run the main() function
if __name__ == "__main__":
    main()

# Problem description:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

 

# Constraints:

#     n == nums.length
#     1 <= n <= 5 * 104
#     -109 <= nums[i] <= 109

 

# Follow-up: Could you solve the problem in linear time and in O(1) space?