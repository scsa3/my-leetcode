class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff_indices = []
        counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
                counter += 1
                if counter == 2:
                    next_i = i + 1
                    if next_i < len(s1) and s1[next_i:] != s2[next_i:]:
                        return False
                    break
        if len(diff_indices) < 2:
            return False

        index0 = diff_indices[0]
        index1 = diff_indices[1]

        return s1[index0] == s2[index1] and s1[index1] == s2[index0]
