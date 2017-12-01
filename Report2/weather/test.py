import matplotlib.pyplot as plt
l50 = [66,63,66,63,68]
l40 = [63,69,67,67,64]
l30 = [74,66,71,68,63]
l20 = [65,69,66,71,66]
l10 = [66,62,64,68,61]
l5 = [68,68,62,64,65]
l60 = [63,71,60,71,65]
l80 = [67,64,61,69,68]
l100 = [62,70,65,60,65]

def ave(l):
	return sum(l)/len(l)

#print "100:{6},80:{7},60:{8},50:{0},40:{1},30:{2},20:{3},10:{4},5:{5}".format(ave(l50),ave(l40),ave(l30),ave(l20),ave(l10),ave(l5),ave(l100),ave(l80),ave(l60))


labels=["Decision Tree","Random Forest","Neural Network","Nearest Neighbours","Gradient Boosting"]

#Precision results for differnt training set sizes
trainsize = [0.5,0.4,0.2,0.6,0.8,0.7,0.3]
class1 = [0.6805,0.685353,0.6457108,0.70170168,0.719244,0.70126,0.6569332]
class2 = [0.76877,0.746519,0.717598,0.7661906,0.7996902,0.781675,0.7283976]
class3 = [0.43075,0.4143546,0.29878,0.52461,0.4437457,0.5973106,0.4841923]
class4 = [0.8563885,0.854477,0.774818,0.876816,0.87642998,0.88074298,0.849490]
class5 = [0.74323,0.73584,0.7306935,0.754201128,0.74621,0.73804472,0.7318617]
#recalls= [[0.58364,0.592405],[0.644536,0.6273754],[0.391637],[0.366699],[0.563074]]



plt.plot(trainsize,class1,'yo',label="Decision Tree")
plt.plot(trainsize,class2,'go',label="Random Forest")
plt.plot(trainsize,class3,'ro',label="Neural Network")
plt.plot(trainsize,class4,'bo',label="Nearest Neighbours")
plt.plot(trainsize,class5,'co',label="Gradient Boosting")
plt.xlabel("Training Set Size")
plt.ylabel("Precision")
plt.title("Precision vs Training set size")
plt.legend(loc=4)
plt.xlim(0,1)
plt.ylim(0,1)
plt.savefig("trainacc.png",dpi=512)
