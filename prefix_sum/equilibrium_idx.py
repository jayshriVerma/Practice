def equilibriumPoint(arr):
    pref_sum = 0
    total = sum(arr)

    # Iterate pivot over all the elements
    # of the array and till prefSum != suffSum
    for pivot in range(len(arr)):
        suff_sum = total - pref_sum - arr[pivot]
        if pref_sum == suff_sum:
            return pivot
        pref_sum  += arr[pivot] # Update prefSum for the next pivot

    return -1

if __name__ == "__main__":
    print(equilibriumPoint([1, 7, 3, 6, 5, 6]))