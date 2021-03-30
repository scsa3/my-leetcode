from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = dict()
        for index, a_score in enumerate(sorted_score):
            rank = index + 1
            if rank == 1:
                rank_map[a_score] = "Gold Medal"
            elif rank == 2:
                rank_map[a_score] = "Silver Medal"
            elif rank == 3:
                rank_map[a_score] = "Bronze Medal"
            else:
                rank_map[a_score] = str(rank)

        result = list()
        for a_score in score:
            rank = rank_map[a_score]
            result.append(rank)
        return result
