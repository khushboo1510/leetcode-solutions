"""
https://leetcode.com/problems/most-common-word/

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        wordsDict = {}
        words = re.sub(r'[^\w]',' ',paragraph.lower()).split()

        for word in words:
            
            if word not in banned:
                wordsDict[word] = wordsDict.get(word, 0) + 1
        
        return max(wordsDict.items(), key=operator.itemgetter(1))[0]