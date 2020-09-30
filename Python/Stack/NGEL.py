
# @author
# Aakash.Verma

# Problem: Given an array, print the Next Greater Element (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element
# 		 on the left side of x in array. Elements for which no greater element exist,
# 		 consider next greater element as -1.


def nextGreaterElementToLeft(arr, n):
	s = []
	v = []
	s.append(arr[0])
	v.append(-1)

	for i in range(1, n):

		if(len(s) == 0):
			v.append(-1)

		elif(s[-1] > arr[i]):
			v.append(s[-1])
			s.append(arr[i])

		else:

			while(len(s) != 0 and s[-1] < arr[i]):
				s.pop()

			if len(s) == 0 :
				v.append(-1)

			else:
				v.append(s[-1])
			s.append(arr[i])

	return v

if __name__ == '__main__':

	arr = [7, 8, 1, 4]
	ans = nextGreaterElementToLeft(arr, len(arr))
	print(ans)