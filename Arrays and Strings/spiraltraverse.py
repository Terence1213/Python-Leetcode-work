from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_num = 0
        col_num = 0
        max_row = len(matrix) - 1
        max_col = len(matrix[0]) - 1

        new_list = []

        direction = "right"

        boxes_checked = [[False] * (max_col + 1) for _ in range(max_row + 1)]

        while len(new_list) < (max_row + 1) * (max_col + 1):
            new_list.append(matrix[row_num][col_num])
            boxes_checked[row_num][col_num] = True
            if direction == "right":
                # Either turn down, if we aren't at the edge then just go straight right.
                if col_num == max_col or boxes_checked[row_num][col_num + 1] == True:
                    row_num += 1
                    direction = "down"
                else:
                    col_num += 1
            
            elif direction == "down":
                # Either turn left, if we aren't at the edge then just go straight down.
                if row_num == max_row or boxes_checked[row_num + 1][col_num] == True:
                    col_num -= 1
                    direction = "left"
                else:
                    row_num += 1
            
            elif direction == "left":
                # Either turn up, if we aren't at the edge then just go straight left.
                if col_num == 0 or boxes_checked[row_num][col_num - 1] == True:
                    row_num -= 1
                    direction = "up"
                else:
                    col_num -= 1
            
            elif direction == "up":
                # Either turn right, if we aren't at the edge then just go straight right.
                if row_num == 0 or boxes_checked[row_num - 1][col_num] == True:
                    col_num += 1
                    direction = "right"
                else:
                    row_num -= 1
        
        return new_list