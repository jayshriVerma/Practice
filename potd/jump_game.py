def jumps(nums: list[int]) -> bool:
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True

def jumps_way(nums: list[int]) -> bool:
    right = 0
    last = len(nums) - 1
    for i in range(len(nums) - 1):
        if i > right:
            return False
        if i + nums[i] > right:
            right = i + nums[i]
        if right >= last:
            return True    

if __name__ == "__main__":
    print(jumps([2, 3, 1, 1, 4])) # Output: True
    print(jumps([3, 2, 1, 0, 4])) # Output: False