from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = self.getRow(rowIndex - 1)
        row = [1]

        for i in range(0, len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])

        row.append(1)

        return row