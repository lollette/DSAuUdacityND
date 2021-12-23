# Problem 3: Rearrange Array Elements


## Reasoning

	In this problem, we need to rearrange array alements so as to form two number such that their sum is maximum.

	Maximum number can be formed given digits `(0-9)` when the largest digit appears first, second largest digit appears second, 
	ans so on.

	We follow the same idea to solve this problem.

	First step is to sort the array. For this we choose to use the counting sort algorithm since we have a specific positive and 		small range. So this step takes `O(n+m)` where `n` is the number of elements in input array and `m` is the range of input.
	==> `O(n)`

	The space is also proportional to the range of data and the number of elemets since we need to create two arrays one for the 		keys and one which will contain the ordered elements. So, the space complexity is `O(n+m)` ==> `O(n)`.

	Once the array is sorted, we can construct two numbers by picking alternating digits from the array.

	the first number will be filled with digits at the even indices and the second number with digits at the odd indices.

	this step is done in `O(n)` where `n` is the number of elements in input array and does not need extra space.

	So the whole program has `O(n)` time complexity and `O(n)` space complexity.

	
