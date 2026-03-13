import math

def minNumberOfSeconds(mountainHeight, workerTimes):
    
    def canFinish(time):
        total = 0
        
        for w in workerTimes:
            k = int((-1 + math.sqrt(1 + 8 * time / w)) // 2)
            total += k
            
            if total >= mountainHeight:
                return True
                
        return False
    
    left = 0
    right = 10**18
    
    while left < right:
        mid = (left + right) // 2
        
        if canFinish(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

if __name__ == "__main__":
    print(minNumberOfSeconds(4, [2, 1, 1])) # Output: 3

# Algorithm
# Binary search time
# For each time, compute how much height all workers can remove
# If ≥ mountainHeight, reduce time.

# 3296. Minimum Number of Seconds to Make Mountain Height Zero 
# Input: mountainHeight = 4, workerTimes = [2,1,1] Output: 3 
# Explanation: One way the height of the mountain can be reduced to 0 is: 
# Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
# Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2 = 3 seconds. 
# Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
# Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.  

# Total time for k units:w(1+2+3+...+k)=w⋅k(k+1)​/2<=T solve for k gives k=⌊2−1+1+8T/w√/2⌋  
# Workers operate in parallel, so instead of deciding the exact work distribution, can binary search on the minimum time required.
# For a given time T, calculate how many mountain units each worker can remove.
# Since the time per unit increases linearly (w, 2w, 3w...), the total time for k units becomes w * k(k+1)/2.
# find the largest k such that this value is ≤ T, sum this for all workers, and check if the total height removed reaches the mountain height.
