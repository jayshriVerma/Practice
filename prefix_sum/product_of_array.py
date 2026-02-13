# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation

def productExceptSelf(nums):
    n = len(nums)
    left, right = [0]*n, [0]*n
    l, r = 1, 1
    for i, num in enumerate(nums):
        left[i] = l
        j = -i-1
        right[j] = r
        l *= nums[i]
        r *= nums[j]
    return [l*r for l,r in zip(left, right)]



# l= [1,1,2,6]
# r=[24,12,4,1]
# so after setting first element of l and r as 1, later we are updating with product of previous element [1,2,3,4]
# l=[1,1,1*2,,1*2*3]
# r=[2*3*4,3*4,4,1] so leaving the last one i.e 1 as starting from right first element right is 1 in place of 4 then 4, then 3*4, then 2*3*4
# so final result is the product of 1*24 ,1*12,2*4,6*1 so the output is  [24,12,8,6]

if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
    print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]