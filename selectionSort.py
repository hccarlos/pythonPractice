import datetime
import random


def selectionSort(array):
	for i in range(0,len(array)):
		minIndex = i
		for index, element in enumerate(array[i:],start=i):
			if element < array[minIndex]:
				minIndex = index
		temp = array[i]
		array[i] = array[minIndex]
		array[minIndex] = temp

def populateList(numElements):
	testList = []
	for i in range(0,numElements):
		testList.append(int(round(random.random()*10000)))
	return testList

testArray = populateList(100)
t1 = datetime.datetime.now().time()
print t1
print t1.microsecond
selectionSort(testArray)
t2 = datetime.datetime.now().time()
print t2
print t2.microsecond

print 'Run time for selectionSort is ' + str(t2.microsecond - t1.microsecond) + ' microseconds'
print testArray