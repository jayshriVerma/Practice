def restoreIpAddresses(s):
    res = []
    n = len(s)

    def backtrack(start, parts, path):
        # If 4 parts are formed and string is used completely
        if parts == 4 and start == n:
            res.append(".".join(path))
            return
        
        # If parts exceed or string finished early
        if parts == 4 or start == n:
            return

        # Try segments of length 1 to 3
        for l in range(1, 4):
            if start + l > n:
                break
            
            segment = s[start:start+l]

            # Avoid leading zero
            if segment[0] == '0' and l > 1:
                continue

            # Check valid range
            if int(segment) <= 255:
                backtrack(start + l, parts + 1, path + [segment])

    backtrack(0, 0, [])
    return res
if __name__ == "__main__":
    print(restoreIpAddresses("255678166")) # Output: ['25.56.78.166', '255.6.78.166', '255.67.8.166', '255.67.81.66']


# The algorithm systematically tries all possible splits but stops early when:
# segment > 255
# segment has leading zero
# more than 4 parts formed
# string finished too early
# This prunes invalid paths quickly.

# Complexity
# Time: 𝑂(3^4) because of the 4 nested loops for 4 segments, and each segment can be at most 3 digits (0-255). In practice, this is a constant time operation since IP addresses have a fixed format.
# Space:  O(1) excluding output.
# Here, how the backtracking algorithm generates the valid IP addresses step by step. The key idea is:
# An IP address has 4 parts.
# Each part must be 0–255.
# Each part can have 1 to 3 digits.
# No leading zeros unless the number is exactly "0".
# Backtracking means trying possibilities and undoing choices when they become invalid.
# Recursion tree for input "255678166":

    #             ""
    #     /        |        \
    #    2        25        255
    #   ...       |         /  \
    #             56       6    67
    #              |       |     |
    #             78      78     8
    #              |       |     |
    #             166     166   166