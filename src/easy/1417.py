class Solution:
    def reformat(self, s: str) -> str:
        alphabet = []
        numberic = []

        for c in s:
            if c.isalpha():
                alphabet.append(c)
            else:
                numberic.append(c)

        alpha_len = len(alphabet)
        number_len = len(numberic)
        if abs(alpha_len - number_len) > 1:
            return ""
        result = ""
        if alpha_len >= number_len:
            for i, v in enumerate(numberic):
                result += alphabet[i]
                result += v
            if alpha_len > number_len:
                result += alphabet[-1]
        else:
            for i, v in enumerate(alphabet):
                result += numberic[i]
                result += v
            result += numberic[-1]

        return result