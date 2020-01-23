class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        for i, x in enumerate(sorted(costs, key=lambda x: x[0] - x[1])):
            total += x[0] if i < len(costs) / 2 else x[1]

        return total