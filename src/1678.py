class Solution:
    def interpret(self, command: str) -> str:
        cache = ""
        result = ""
        for c in command:
            if c == "G":
                result += "G"
            elif c == ")":
                if cache == "(":
                    result += "o"
                else:
                    result += "al"
                cache = ""
            else:
                cache += c
        return result
