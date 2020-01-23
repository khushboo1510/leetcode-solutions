class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        d = collections.defaultdict(list)
        lst = []

        for i in range(len(groupSizes)):
            if len(d[groupSizes[i]]) == groupSizes[i]:
                lst.append(d[groupSizes[i]])
                d[groupSizes[i]] = []
            d[groupSizes[i]].append(i)

        for key, value in d.items():
            lst.append(value)

        return lst

