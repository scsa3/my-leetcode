class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = {(0, 0)}
        now = [0, 0]
        move_map = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0],
        }

        for c in path:
            move = move_map[c]
            now[0] += move[0]
            now[1] += move[1]
            now_tuple = (now[0], now[1])
            if now_tuple in locations:
                return True
            locations.add(now_tuple)
        return False
