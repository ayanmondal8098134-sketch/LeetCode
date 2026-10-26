from collections import deque


class Solution(object):

  def countIslands(self, grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: int
    """
    m, n = len(grid), len(grid[0])
    valid_islands = 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] > 0:
          # Start BFS traversal for this island
          total_val = 0
          queue = deque([(i, j)])
          total_val += grid[i][j]
          grid[i][j] = 0  # Mark visited

          while queue:
            r, c = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
              nr, nc = r + dr, c + dc
              if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                total_val += grid[nr][nc]
                grid[nr][nc] = 0  # Mark visited
                queue.append((nr, nc))

          if total_val % k == 0:
            valid_islands += 1

    return valid_islands