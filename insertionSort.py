import datetime
import random


def insertionSort(array):
	if len(array) < 2:
		return array
	else:
		for n in range(1,len(array)):
			for i in range(n, 0, -1):
				if(array[i]<array[i-1]):
					array[i],array[i-1] = array[i-1],array[i]





def populateList(numElements):
	testList = []
	for i in range(0,numElements):
		testList.append(int(round(random.random()*10000)))
	return testList

testArray = populateList(30)
t1 = datetime.datetime.now().time()
print t1
print t1.microsecond
insertionSort(testArray)
t2 = datetime.datetime.now().time()
print t2
print t2.microsecond

print 'Run time for insertionSort is ' + str(t2.microsecond - t1.microsecond) + ' microseconds'
print testArray