from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # If the number of lists we've gone through is odd, then we move up, if the number of lists we've gone through is even, we move down.
        # If we are going top right, then the x value is increasing, and the y value is decreasing.
        # If we are going bottom left, the x value is decreasing, and y value is increasing

        direction = 1 # Direction value 1 represents top right, direction value 2 represents bottom left.
        current_x = 0
        current_y = 0
        y_length = len(mat[0])
        x_length = len(mat)
        
        new_list = []

        # Every time we rotate, since we need to change the current x and y, this is how the logic will work:
        # If we were previously moving towards top right, then either the x increases b one, or the y increases by one
        # If we were previously moving towards bottom left, then either the y increases by one, or the x increases b one
        # So practically it doesn't matter whether we were moving towards bottom left or rop right, it just matters whether 
        # we're going to increase the y or the x by one, depending on whether the array has space on the y or on the x axis.


        list_complete = False
        while list_complete == False:
            while True:
                
                new_list.append(mat[current_x][current_y])
                
                print(current_x)
                print(current_y)
                
                # If we can't go neither right nor down, then we've gone through the whole list.
                if current_x >= x_length - 1 or current_y >= y_length - 1:
                    break
                
                if current_x <= 0 or current_y <= 0:
                    break

                if direction == 1:
                    # x value increases, y value decreases
                    current_x += 1
                    current_y -= 1
                else:
                    # x value decreases, y increases
                    current_x -= 1
                    current_y += 1

            print()
            print("Rotation!")
            print()
            
            if direction == 1:
                # Priority is going right, so first we check whether there exists an index of one greater than the current x
                if current_x + 1 <= x_length - 1:
                    # We will go to the right in this case:
                    current_x += 1
                    direction = 2
                elif current_y + 1 <= y_length - 1:
                    # We will go down
                    current_y += 1
                    direction = 2
                
            elif direction == 2:
                if current_y + 1 <= y_length - 1:
                    current_y += 1
                    direction = 1
                elif current_x + 1 <= x_length - 1:
                    current_x += 1
                    direction = 1
                
                
        
        return new_list
    
class SolutionTwo:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        direction = 1  # 1 = top right, 2 = bottom left
        current_x = 0 # Note that x is the row number 
        current_y = 0 # Note that y is the column number.
        y_length = len(mat[0])
        x_length = len(mat)

        new_list = []

        while len(new_list) < x_length * y_length:
            new_list.append(mat[current_x][current_y])

            if direction == 1:  # going top right
                if current_y == y_length - 1:  # hit right edge
                    current_x += 1
                    direction = 2
                elif current_x == 0:  # hit top edge
                    current_y += 1
                    direction = 2
                else:  # normal move
                    current_x -= 1
                    current_y += 1

            else:  # direction == 2, going bottom left
                if current_x == x_length - 1:  # hit bottom edge
                    current_y += 1
                    direction = 1
                elif current_y == 0:  # hit left edge
                    current_x += 1
                    direction = 1
                else:  # normal move
                    current_x += 1
                    current_y -= 1

        return new_list
    
class SolutionThree:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        direction = 1  # 1 = top right, 2 = bottom left
        row_num = 0 # Note that x is the row number 
        col_num = 0 # Note that y is the column number.
        column_amount = len(mat[0])
        row_amount = len(mat)

        new_list = []

        # Keep looping until we've searched through the whole 2d list.
        while len(new_list) < row_amount * column_amount:
            new_list.append(mat[row_num][col_num])

            if direction == 1:
                # First we check if we have to turn, then we actually perform a normal movement. If we're moving top right, then we have to check whether we hit the top or the right side.
                if col_num >= column_amount - 1:
                    row_num += 1
                    direction = 2
                elif row_num == 0:
                    col_num += 1
                    direction = 2
                else:
                    col_num += 1
                    row_num -= 1
            else:
                # If we're moving bottom left, we have the check whether we hit the bottom or the left side.
                if row_num >= row_amount - 1:
                    col_num += 1
                    direction = 1
                elif col_num == 0:
                    row_num += 1
                    direction = 1
                else:
                    col_num -= 1
                    row_num += 1
        
        return new_list