from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
                
        rows = []
        for i in range(0, rowIndex + 1):
            # The value of i will help us determine how many numbers there are in the current row.
            if i == 0:
                rows.append([1])
            else:
                # We have to add a 1 at the start of the list, a 1 at the end of the list, and the sums of the current row between.
                new_row = []
                new_row.append(1)
                if len(rows[i - 1]) > 1:
                    # If the length is greater than just 1 number (which would be one), then we have 2 numbers to add together. Note that we stop at length - 1 since we're adding with the next index.
                    for x in range(0, len(rows[i - 1]) - 1):
                        new_row.append(rows[i-1][x] + rows[i-1][x + 1])
                
                new_row.append(1)

                rows.append(new_row)
        
        return rows[rowIndex]

