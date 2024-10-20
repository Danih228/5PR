def fill_matrix_random(matrix):
  
  rows = len(matrix)
  columns = len(matrix[0])
  for i in range(rows):
    for j in range(columns):
      matrix[i][j] = random.randint(0, 100)
