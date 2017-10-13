import random
import matplotlib.pyplot as plt
listt = []
i=0
while i<= 10000:
	listt.append(random.normalvariate(0,1))
	i += 1

plt.hist(listt, 100, normed = 1)
plt.show()

