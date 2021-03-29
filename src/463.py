from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        wall_count = 0
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if self.is_up_wall(x, y, grid):
                    wall_count += 1
                if self.is_down_wall(x, y, max_y, grid):
                    wall_count += 1
                if self.is_left_wall(x, y, grid):
                    wall_count += 1
                if self.is_right_wall(x, y, max_x, grid):
                    wall_count += 1
        return wall_count

    @staticmethod
    def is_up_wall(x, y, grid) -> bool:
        if grid[y][x] == 0:
            return False
        if y == 0:
            return True
        if grid[y - 1][x] == 0:
            return True
        else:
            return False

    @staticmethod
    def is_down_wall(x, y, max_y, grid) -> bool:
        if grid[y][x] == 0:
            return False
        if y == max_y:
            return True
        if grid[y + 1][x] == 0:
            return True
        else:
            return False

    @staticmethod
    def is_left_wall(x, y, grid) -> bool:
        if grid[y][x] == 0:
            return False
        if x == 0:
            return True
        if grid[y][x - 1] == 0:
            return True
        else:
            return False

    @staticmethod
    def is_right_wall(x, y, max_x, grid) -> bool:
        if grid[y][x] == 0:
            return False
        if x == max_x:
            return True
        if grid[y][x + 1] == 0:
            return True
        else:
            return False


