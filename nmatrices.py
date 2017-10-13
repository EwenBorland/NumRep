import numpy

#(1,2)(a) = (3)
#(3,4)(b) = (4)

#ax=b
#=> x = inv(a)*b
def simulteq(a,x,b):
	x1 = numpy.dot(numpy.linalg.inv(a), b)
	for i in range(len(x)):
		print(str(x[i])+" = "+str(x1[i]))
		
testMatA = [[2,2],[4,5]] 
testMatx = [["h"],["l"]]
testMatB = [[4],[8]]

simulteq(testMatA,testMatx,testMatB)

