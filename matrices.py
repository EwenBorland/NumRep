class Matrix:
	#initialisation, takes a list of lists, each sublist is equivalent to a row
	def __init__(self,list_lists):
		#loop to check each row has the same number of columns
		for i in list_lists:
			if len(i) != len(list_lists[0]):
				print("rows do not have an equal number of columns")
				thing = False
			else: thing = True
		if thing:
			self.data = list_lists
			self.cols = len(list_lists)
			self.rows = len(list_lists[0])
	
	# function to check if matrix A can be added/subtracted from self, returns boolean
	def checksumMat(self,A):
		if self.rows  == A.rows and self.cols == A.cols:
			return True
		else: 
			print("cannot sum matrices")
			return False
	
	# function to check if matrix A can be multipled with self, returns boolean	
	def checkmultMat(self ,A):
		if self.cols == A.rows:
			return True
		else: 
			print("cannot multiply matrices")
			return False
		
		
	def addMat(self,A):
		newMatlist_lists = []
		if self.checksumMat(A):
			for rownum in range(len(self.data)):
				newMatlist= []
				for colnum in range(len(self.data[rownum])):
					newMatlist.append(self.data[rownum][colnum] + A.data[rownum][colnum])
				newMatlist_lists.append(newMatlist)
		return Matrix(newMatlist_lists)
	
	def subMat(self,A):
		newMatlist_lists = []
		if self.checksumMat(A):
			for rownum in range(len(self.data)):
				newMatlist= []
				for colnum in range(len(self.data[rownum])):
					newMatlist.append(self.data[rownum][colnum] - A.data[rownum][colnum])
				newMatlist_lists.append(newMatlist)
			return Matrix(newMatlist_lists)
	
	# determinant function
	#m[y][x]
	def detMat(self):
		m = self.data
		if len(m) == 2:
			return m[0][0]*m[1][1] - m[1][0]*m[0][1]
		det = 0
		for i in range(self.cols):
			det += ((-1)**i) # nope
			
			


# (a,b)	x (1,2) = (a1 + b3, a2 + b4)
# (c,d)   (3,4)   (c1 + d3, c2 + d4)
#
#	
	def multMat(self,A):
		newMatlist_lists = []
		if self.checkmultMat(A):
			# for each row in self, for colsnum in A, make a entry in new row
			for row in self.data:
				newrow = []
				for i in range(A.cols):
					summed = 0
					for j in range(len(row)):
						summed += row[j]*A.data[j][i]
					newrow.append(summed)
				newMatlist_lists.append(newrow)
		return Matrix(newMatlist_lists)
			
	


#test stuff
matrixlist1 = [[1,2,3],[4,5,6],[7,8,9]]
matrixlist2 = [[3,2,1],[6,5,4],[9,8,7]]

matA = Matrix(matrixlist1)
matB = Matrix(matrixlist2)


matC = matA.multMat(matB)
print(matC.data)
