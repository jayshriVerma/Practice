from typing import List


def valid_triangle(nums:List[int]) -> int:
    nums.sort()
    n, count = len(nums), 0
    for k in range(n- 1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                count += (j - i)
                j -= 1
            else:
                i += 1
    return count


if __name__ == "__main__":
    print(valid_triangle([2,2,3,4])) # Output: 3
    print(valid_triangle([4,2,3,4])) # Output: 4
    print(valid_triangle([1,1,1,1])) # Output: 4
    print(valid_triangle([1,2,3])) # Output: 0