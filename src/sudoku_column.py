def column_correct(sudoku: list, column_no: int):
  column_length = len(sudoku) # column length is the same as the number of rows in sudoku
  number = 1 # Variable will be used to check for each number 1-9
  while number <= column_length:
    row = 0 # Variable to move through each row
    count = 0
    while row < column_length:
      if number == sudoku[row] [column_no]: # Check to see if numbers 1-9 are in the column
        count += 1
      row += 1
    if count > 1:
        return False
    number += 1
  return True # If loop completes then each number was found only once in the column, return true. 

