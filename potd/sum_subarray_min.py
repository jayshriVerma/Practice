from typing import List
def sumSubarrayMins(self, arr: List[int]) -> int:
    # instead of finding the minimum element of each subarray, we find that the how many subarays have that element as their minimum value,
    # then multiply by the elements value to get the next smaller element
    mod = 10**9+7
    n = len(arr)
    left =[-1] *n
    right =[n] *n
    stk = []
    for i, v in enumerate(arr):
        while stk and arr[stk[-1]] >= v:
            stk.pop()
        if stk:
            left[i] = stk[-1]
        stk.append(i)        
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] > arr[i]:
            stk.pop()
        if stk:
            right[i] = stk[-1]
        stk.append(i)
    return sum((i - left[i]) * (right[i] - i) * v for i, v in enumerate(arr)) % mod

if __name__ == "__main__":
    print(sumSubarrayMins(None, [3,1,2,4])) # Output: 17