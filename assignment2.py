matrix=[['x','o','x'],['x','o','x'],['o','x','o']]

def check_rows(matrix):
	for i in matrix:
		if i==['x','x','x'] or i==['o','o','o']:
			return True
		return False

print check_rows(matrix)

def check_columns(matrix):
	for col in range(0,3):
		if matrix[0][col]==matrix[1][col]==matrix[2][col]:
			return True
		return False

print check_columns (matrix)
		
def check_diagonals(matrix):
	for i in range(0,2):
		if matrix[0][i]==matrix[1][i+1]==matrix[2][i+2]:
			return True
		elif matrix[0][2]==matrix[1][1]==matrix[2][0]:
				return True
		return False
print check_diagonals(matrix)

		