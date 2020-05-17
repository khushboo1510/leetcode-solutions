"""
https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.
"""
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        res = []
        for i, favoriteCompany in enumerate(favoriteCompanies):
            favoriteCompanies[i] = sorted(favoriteCompany)
        print(favoriteCompanies)
        for i, favoriteCompany in enumerate(favoriteCompanies):
            count = 0
            for fc in favoriteCompanies:
                if set(favoriteCompany).issubset(set(fc)):
                    count += 1
            
            if count == 1:
                res.append(i)
                
        return res