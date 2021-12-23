# Problem 2: Search in a Rotated Sorted Array


## Reasoning

	The solution for this problem is divided into two steps.

	The first step is to find the pivot around which the array was rotated.

	For this we recursively use the concept of binary search to find the unique element
	for which next element to it is smaller than it and get the pivot  in `O(logn)` time

	If the pivot position is found, we test if its value corresponds to the desired element we return the pivot

	If not we call binary search for one of the two sub-arrays.

	On the other hand, if the pivot does not exist that means that the array has not been rotated and
	we call binary search for the whole arrays

	The second step is also done in `O(logn)` time

	So in the worst case, the algorithm is `O(logn)`.

	The space taken by the algorithm is the same for any input array so `O(1)`
