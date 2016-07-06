import datetime
import random

def bubbleSort(array):
	for i in range(0,len(array)):
		for j in range(0,len(array)-1-i):
			if array[j+1] < array[j]:
				temp = array[j+1]
				array[j+1] = array[j]
				array[j] = temp


def populateList(numElements):
	testList = []
	for i in range(0,numElements):
		testList.append(int(round(random.random()*10000)))
	return testList

testArray = populateList(100)
t1 = datetime.datetime.now().time()
print t1
print t1.microsecond
bubbleSort(testArray)
t2 = datetime.datetime.now().time()
print t2
print t2.microsecond

print 'Run time for bubbleSort is ' + str(t2.microsecond - t1.microsecond) + ' microseconds'