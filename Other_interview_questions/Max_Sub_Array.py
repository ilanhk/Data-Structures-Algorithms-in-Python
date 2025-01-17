# List: Max Sub Array ( ** Interview Question)
# Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.

# Remember to also account for an array with 0 items.



# Function Signature:

# def max_subarray(nums):


# Input:

# A list of integers nums.



# Output:

# An integer representing the sum of the contiguous subarray with the largest sum.



# Example:

# max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# Output: 6
# Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.

# WRITE THE MAX_SUBARRAY FUNCTION HERE #
def max_subarray(nums):
    if not nums:
        return 0
 
    max_sum = current_sum = nums[0]
 
    for num in nums[1:]:
        current_sum = max(num, current_sum + num) # current_sum is updated to be the maximum of either the current number alone (num) or the sum of current_sum plus num. This decision determines whether to start a new subarray or to continue with the existing one.
        max_sum = max(max_sum, current_sum) # max_sum is updated to be the maximum of itself and current_sum, ensuring it always holds the highest sum of any subarray found so far.
 
    return max_sum
    
########################################



# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)  

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2) 

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3) 


"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1
    
"""