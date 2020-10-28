# https://leetcode.com/problems/search-suggestions-system/
    
# Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of searchWord is typed. 

#Solution 1 - In O(n ^ 2) time by using previous results
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         result, prev = [], products
#         s = ''
#         for i, ch in enumerate(searchWord):
#             s += ch
#             res, count = [], 0
#             for product in prev:
#                 if product[:i + 1] == s:
#                     res.append(product)
#                     count += 1
#             prev = res
#             result.append(res[:3])
#         return result
    
#Solution 2 - Trie
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node = self.root
    
    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if node.n < 3:
                node.words.append(word)
                node.n += 1
    def find_words_with_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return ''
            node = node.children[ch]
        return node.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result, trie = [], Trie()
        
        for word in products:
            trie.add_word(word)
        s = ''
        for ch in searchWord:
            s += ch
            result.append(trie.find_words_with_prefix(s))
        return result
