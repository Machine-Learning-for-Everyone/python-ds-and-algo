# 1. Array
import array as arr

def get_array():
	ar = []
	for i in range(1,11):
		ar.append(i)
	return ar

class NewArray:
	def __init__(self, length):
		self.length = length
	def get_array(self):
		ar = []
		for i in range(1, self.length):
			ar.append(i)
		return ar



newArray = NewArray(3)

## Array Operations


