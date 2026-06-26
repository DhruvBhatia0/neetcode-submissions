class Solution:

    def __init__(self):
        self.visited = set()

    def discover(self, grid, row_idx, col_idx):
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        neighbours = [
            (row_idx + dr, col_idx + dc)
            for dr, dc in directions
        ]

        for n in neighbours:
            x, y = n
            if -1 < x < len(grid) and -1 < y < len(grid[0]):
                if grid[x][y] == "1" and (x,y) not in self.visited:
                    self.visited.add((x,y))
                    self.discover(grid, x, y)
                self.visited.add((x,y))
        


    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0

        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):

                if (row_idx, col_idx) in self.visited or val == "0":
                    self.visited.add((row_idx, col_idx))
                    continue
                
                self.visited.add((row_idx, col_idx))

                # discover everything
                self.discover(grid, row_idx, col_idx)

                island_count += 1
        
        return island_count

                