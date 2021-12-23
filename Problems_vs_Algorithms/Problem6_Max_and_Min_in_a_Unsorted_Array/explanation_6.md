# Problem 6: Max and Min in a Unsorted Array


## Reasoning

	The requirements for this problem are to find the min and the max in a unsorted array in `O(n)` and in a single travesal.

	The idea is to initialize the min and the max value with the value contained in the index `0` (first value of the array)
	
	Then, as we move forward in the array, we check whether the current value is greater than the current max and thus 
	update the max or the opposite if the value is less than the min update this one.

	For this approach we do not need any extra space, so the space complexity is constant `O(1)`.

	

	
