from collections import deque


def orangesRot(mat):
    """multi-source BFS (Breadth-First Search) problem
        Think of rotten oranges as spreading infection.

        At time = 0 → all initially rotten oranges
        At time = 1 → they rot their neighbors
        At time = 2 → newly rotten ones spread further
        and so on...
        BFS helps simulate this level-by-level spread in time."""
    r, c = len(mat), len(mat[0])
    queue = deque()
    fresh = 0
    
    # Step 1: Initialize queue and count fresh oranges
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 2:
                queue.append((i, j))
            elif mat[i][j] == 1:
                fresh += 1
    
    # If no fresh oranges
    if fresh == 0:
        return 0
    
    time = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Step 2: BFS
    while queue: # queue contains all currently rotten oranges,Initially → all rotten oranges at time 0
        size = len(queue) # This freezes the number of oranges to process for this minute only
        rotten_this_round = False
        
        for _ in range(size): # We process only the oranges that were rotten at the start of this minute
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy # this checks the up, down, left, right neighbors
                
                if 0 <= nx < r and 0 <= ny < c and mat[nx][ny] == 1: # stay inside the grid
                    mat[nx][ny] = 2 # mark it rotten
                    queue.append((nx, ny)) # Add it to queue → it will spread infection next minute
                    fresh -= 1             # Decrease fresh count
                    rotten_this_round = True # Mark that something changed this round
        
        if rotten_this_round: # Only increase time if at least one orange rotted
            time += 1
    
    # Step 3: Check result
    return time if fresh == 0 else -1

# 🧭 994. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values: 
# 0 representing an empty cell, 1 representing a fresh orange, or 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# BFS + queue
# Time complexity O(m*n), space O(m*n) in worst case when all oranges are rotten and added to queue
# Initialize queue with rotten oranges, count fresh oranges 
# For each minute, process all rotten oranges in queue, rot adjacent fresh oranges and add them to queue
# size = len(queue) → process one time layer
# Each loop = 1 minute
# Add newly rotten oranges to queue
# Increase time only if something rots
# At the end:
# If fresh == 0 → return time
# Else → return -1
# Key Insight:
# Queue = current rotten oranges
# Each loop = 1 unit time
# New rotten oranges go to queue → next round spread

if __name__ == "__main__":
    print(orangesRot([[2,1,1],[1,1,0],[0,1,1]])) # Output: 4
    print(orangesRot([[2,1,1],[0,1,1],[1,0,1]])) # Output: -1
    print(orangesRot([[0,2]]))                    # Output: 0
