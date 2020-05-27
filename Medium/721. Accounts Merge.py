"""
https://leetcode.com/problems/accounts-merge/

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        queue = []
        visited = {}
        arr = [False] * len(accounts)
        result = []
        i = -1
        while 1:
            if not queue:
                if result:  
                    result[i] = [result[i][0]] + sorted(result[i][1:])
                flag = False
                for k, a in enumerate(arr):
                    if not a:
                        queue = accounts[k][1:]
                        result.append([accounts[k][0]])
                        arr[k], flag = True, True
                        i += 1
                        break
                if not flag:
                    break
            account = queue.pop(0)
            if account not in visited:
                for j, acc in enumerate(accounts):
                    if not arr[j] and account in acc:
                        queue.extend(acc[1:])
                        arr[j] = True
                result[i].append(account)
                visited[account] = 1
            
        return result