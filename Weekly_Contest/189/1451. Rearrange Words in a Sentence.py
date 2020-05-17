"""
https://leetcode.com/problems/rearrange-words-in-a-sentence/

Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.
"""

class Solution:
    def arrangeWords(self, text: str) -> str:
        l = text.lower().split(" ")
        text = ' '.join(sorted(l, key = len)).capitalize()
        return text