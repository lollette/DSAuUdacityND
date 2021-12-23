# Problem 4: Dutch National Flag Problem


## Reasoning

	The requirements for this problem are to perform a `O(n)` sorting in  a single travesal.

	The idea is to fix a pivot, which in our case is the element `1` then to swap the other elements around this 
	one depending on whether they are higher or lower than this one.

	To avoid unnecessary swaps, we also add a condition to check if the two elements that we intend to swap 
	are the same or not.

	The sorting is done in `O(n)` where `n` is the number of the elements since we need to check each element once.

	For this approach we do not need any extra space, so the space complexity is constant `O(1)`.

	

	
