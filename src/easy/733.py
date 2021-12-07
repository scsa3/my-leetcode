from typing import List, Tuple


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        if origin_color == newColor:
            return image
        temp_pos = [
            [sr + 1, sc],
            [sr - 1, sc],
            [sr, sc + 1],
            [sr, sc - 1],
        ]

        max_row_index = len(image) - 1
        max_column_index = len(image[0]) - 1
        min_index = 0

        image[sr][sc] = newColor

        for r, c in temp_pos:
            if not r < min_index and not r > max_row_index and not c < min_index and not c > max_column_index and \
                    image[r][c] == origin_color:
                image = self.floodFill(image, r, c, newColor)

        return image


result = Solution().floodFill(
    [[0, 0, 0], [0, 1, 1]],
    1,
    1,
    1,
)
print(result)
