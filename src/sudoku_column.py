def column_correct(sudoku: list, column_no: int):
  column_length = len(sudoku) # column length is the same as the number of rows in sudoku
  number = 1 # Variable will be used to check for each number 1-9
  row = 0 # Variable to move through each row
  checked_number = [] # Store numbers that have already been checked. 
  while number <= column_length:
    while row <= column_length:
      if number == sudoku[row] [column_no]: # Check to see if numbers 1-9 are in the column
        if checked_number.count(number) > 0: # Check to see if any number has been repeated
          return False # If the number is a duplicate return false
        else:
          checked_number.append(number) # If the number is in the column only once, add to checked_number list
        row += 1
    number += 1
    else:
      return False # If any number 1-9 is NOT found in the column return false
  return True # If loop completes then each number was found only once in the column, return true. 
