
def countSubarrays(arr):
        n = len(arr)
        stack,res =[], 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                res += i - idx
            stack.append(i)
            
        while stack:
            idx = stack.pop()
            res += n -idx
        return res


# Subarrays with First Element Minimum      
# Input: arr[] = [1, 2, 1], Output: 5
# Explanation:
# All possible subarrays are:
# [1], [1, 2], [1, 2, 1], [2], [2, 1], [1]
# Valid subarrays are:
# [1], [1, 2], [1, 2, 1], [2], [1] -> total 5

# Subset	Any combination of elements (order preserved but not necessarily contiguous)
# Subarray	Contiguous elements in the array
# Example for [1,2,1]:
# Subsets your code generates:[], [1], [2], [1,2], [1], [1,1], [2,1], [1,2,1]
# But subarrays are only:[1], [1,2], [1,2,1], [2], [2,1], [1]

# Think:"For each element, count how many subarrays start here until a smaller element appears."
# Monotonic stack helps find that boundary in O(n).

if __name__ == "__main__":
    print(countSubarrays([1, 2, 1])) # Output: 5