class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
       
        paragraph = re.sub(r'[^\w\s]',' ',paragraph).lower()
        paragraph = re.sub(' +', ' ', paragraph)
        d = collections.Counter(paragraph.split(" "))
        
        for word in banned:
            if d.get(word):
                d.pop(word)
        
        return max(dict(d).items(), key=operator.itemgetter(1))[0]
        