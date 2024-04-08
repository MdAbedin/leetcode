class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)

        for s in sandwiches:
            if counts[s] == 0: return counts[1-s]
            counts[s] -= 1

        return 0
