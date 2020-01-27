from collections import Counter


def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1_cnt = Counter(word1.lower().replace(' ', ''))
    word2_cnt = Counter(word2.lower().replace(' ', ''))
    return word1_cnt == word2_cnt
