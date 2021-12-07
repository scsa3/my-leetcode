ascii_map = {
    'a': '0',
    'b': '1',
    'c': '2',
    'd': '3',
    'e': '4',
    'f': '5',
    'g': '6',
    'h': '7',
    'i': '8',
    'j': '9',
}


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f = word_to_number(firstWord)
        s = word_to_number(secondWord)
        t = word_to_number(targetWord)

        return (f + s) == t


def word_to_number(word: str) -> int:
    result_s = ''

    for c in word:
        n = ascii_map[c]
        result_s += n

    return int(result_s)
