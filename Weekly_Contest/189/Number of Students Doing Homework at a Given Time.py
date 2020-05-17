class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for st, et in zip(startTime, endTime):
            if st <= queryTime <= et:
                count += 1
        return count