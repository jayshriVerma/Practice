def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
            """hard dp problem, we can use a 3D dp array to store the number of stable binary arrays with i zeros and j ones, and the last element is either 0 or 1.
            dp[i][j][0] = number of arrays with i zeros and j ones ending with 0
            dp[i][j][1] = number of arrays with i zeros and j ones ending with 1
            The transition is based on the last element and the limit condition"""
            MOD = 10**9 + 7
            dp = [[[0, 0] for _ in range(one+1)] for _ in range(zero+1)]

            # Base cases: dp[i][0][0] = 1 for i in range(zero+1) and
            # limit 2 , then  0 , 00 valid but 000 is not valid, so we can only have up to limit number of consecutive 0s or 1s.
            for i in range(min(zero, limit) + 1):
                dp[i][0][0] = 1
            # dp[0][j][1] = 1 for j in range(one+1) since we can have arrays of all 0s or all 1s up to the limit.
            for j in range(min(one, limit) +1):
                dp[0][j][1] = 1


            for i in range(1,zero +1):
                for j in range(1, one+1):
                    if i > limit:
                        dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1] - dp[i-limit-1][j][1])# Subtract If we keep extending zeros, we might create limit+1 consecutive 0s
                    else:
                        dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]

                    dp[i][j][0] = (dp[i][j][0] % MOD + MOD) % MOD

                    if j > limit:
                        dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1] - dp[i][j - limit-1][0])
                    else:
                        dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1]

                    dp[i][j][1] = (dp[i][j][1] % MOD + MOD) % MOD

            
            return (dp[zero][one][0] + dp[zero][one][1]) % MOD

Leetcode 3129. Find All Possible Stable Binary Arrays I
You are given 3 positive integers zero, one, and limit.

A binary array arr is called stable if:
The number of occurrences of 0 in arr is exactly zero.
The number of occurrences of 1 in arr is exactly one.
Each subarray of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.
Since the answer may be very large, return it modulo 10**9 + 7.


Input: zero = 1, one = 2, limit = 1, Output: 1
The only possible stable binary array is [1,0,1].
Note that the binary arrays [1,1,0] and [0,1,1] have subarrays of length 2 with identical elements, 
hence, they are not stable.


Input: zero = 3, one = 3, limit = 2, Output: 14
All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0],
[1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

if __name__ == "__main__":
    print(numberOfStableArrays(1, 2, 1)) # Output: 1
    print(numberOfStableArrays(3, 3, 2)) # Output: 14

Dry Run:
For zero = 1, one = 2, limit = 1:
No two same adjacent elements allowed, so the only valid array is [1,0,1]
Initialization : 
dp[0][1][1] = 1 → [1]
dp[1][0][0] = 1 → [0]
State (1,1) Ending with 0:
            dp[1][1][0] =dp[0][1][0] + dp[0][1][1]= 0 + 1= 1
            array [1,0]
Ending with 1:
     dp[1][1][1] =dp[1][0][0] + dp[1][0][1]= 1 + 0= 1
     [0,1]

state (1,2) Ending with 0:
        dp[1][2][0] =dp[0][2][0] + dp[0][2][1]= 0 + 0= 0
        array [1,1,0] invalid      But limit=1, so [1,1] is invalid → removed. so dp[1][2][0] = 0
Ending with 1: dp[1][2][1] =dp[1][1][0] + dp[1][1][1]- dp[1][0][0] = 1 + 1 - 1 = 1 array [1,0,1]

dp[1][2][0] = 0
dp[1][2][1] = 1 final: 1 ans

Time  : O(zero × one)
Space : O(zero × one)
This is hard because the trick - dp[i-limit-1][j][1] is not obvious. It works by removing sequences that would produce runs longer than limit.
This is a classic DP + sliding window / prefix subtraction trick used in many hard problems.