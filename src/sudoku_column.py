def column_correct(sudoku: list, column_no: int):
  column_length = len(sudoku) # column length is the same as the number of rows in sudoku
  number = 1 # Variable will be used to check for each number 1-9
  checked_number = [] # Store numbers that have already been checked. 
  while number <= column_length:
    row = 0 # Variable to move through each row
    while row < column_length:
      if number == sudoku[row] [column_no]: # Check to see if numbers 1-9 are in the column
        if checked_number.count(number) > 0: # Check to see if any number has been repeated
          return False # If the number is a duplicate return false
        else:
          checked_number.append(number) # If the number is in the column only once, add to checked_number list
          break
      row += 1
    number += 1
  if len(checked_number) < 9:
    return False
  return True # If loop completes then each number was found only once in the column, return true. 

