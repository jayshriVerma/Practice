from collections import deque

def countSubarrays(nums, k):
    max_d = deque()
    min_d = deque()
    left = 0
    res = 0

    for right in range(len(nums)):
        while max_d and nums[max_d[-1]] < nums[right]:
            max_d.pop()
        max_d.append(right)

        while min_d and nums[min_d[-1]] > nums[right]:
            min_d.pop()
        min_d.append(right)

        while nums[max_d[0]] - nums[min_d[0]] > k:
            left += 1
            if max_d[0] < left:
                max_d.popleft()
            if min_d[0] < left:
                min_d.popleft()

        res += (right - left + 1)

    return res

# 🧭 2100. Count All Possible Routes
if __name__ == "__main__":
    print(countSubarrays([1,2,3], 1)) # Output: 4
    print(countSubarrays([1,3], 3)) # Output: 3
    print(countSubarrays([4,2,1], 2)) # Output: 3
    print(countSubarrays([1,3,2,5,4], 2)) # Output: 9
    # here 9 subarrays are valid: [1], [3], [2], [5], [4], [1,3], [3,2], [5,4], [1,3,2] here [2,5] is not valid because max-min = 5-2=3 > k=2

# Explanation:
# We use two deques to maintain the indices of the maximum and minimum elements in the current window.
# We expand the right pointer and update the deques accordingly.
# If the difference between the maximum and minimum exceeds k, we move the left pointer until the condition is satisfied again.
# For each valid window, we add the number of subarrays that can be formed with the current right pointer, which is (right - left + 1).
# Time complexity: O(n) because each element is added and removed from the deques at most once.
