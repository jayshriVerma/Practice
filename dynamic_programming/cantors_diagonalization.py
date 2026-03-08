from typing import List
def findDifferentBinaryString(nums: List[str]) -> str:
        res = []

        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')

        return "".join(res)




if __name__ == "__main__":
    print(findDifferentBinaryString(["01","10"])) # Output: "11"

# Find Unique Binary String
# n strings
# length = n
# need a different string
# Diagonal flip trick: flip the i-th bit of the i-th string to ensure the resulting string is different from all given strings. This guarantees uniqueness because it differs from each string at least in one position.
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.