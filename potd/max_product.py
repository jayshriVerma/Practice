def maxProduct(nums):
    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        cur = nums[i]

        # swap when negative
        if cur < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(cur, max_prod * cur)
        min_prod = min(cur, min_prod * cur)

        result = max(result, max_prod)

    return result

if __name__ == "__main__":
    print(maxProduct([2, 3, -2, 4]))  # Output: 6
    print(maxProduct([-2, 0, -1]))     # Output: 0
    print(maxProduct([-2, 3, -4]))     # Output: 24

# Negative numbers flip signs.
# So at each index, you must track:
# max_product_so_far
# min_product_so_far
# Why track min?
# A negative × negative → big positive
# "Yesterday’s worst can become today’s best" Because negative numbers flip signs,
# track both the maximum and minimum product ending at each index. A previous minimum can become the maximum when multiplied by a negative number.