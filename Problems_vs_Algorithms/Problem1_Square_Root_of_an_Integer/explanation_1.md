# Problem 1: Finding the Square Root of an Integer


## Reasoning

	the problem of finding the square root of a number can be solved using the binary search concept.


	firstly, we define our search interval between `1` and the `number / 2` given that the square root of a number other than 	  zero can neither be zero nor be greater than the half of it.


	Then we calculate the middle of this interval.

	If the middle to square corresponds to the number the function returns the value of the middle and in this case we will have 		found the perfect square root.

	Otherwise if the the middle to square is less than the number, we save a copy of it as the current square root since we need 		the floor and update the lower bound with the value of the `middle + 1`

	if instead the middle to square is greater than the number we update the upper bound with the value of `middle - 1`


	We repeat the search on the new interval until the perfect root is returned or the upper bound is lower than the lower bound 		which in this case the function returns the closest approximation to the perfect square root.



	The runtime complexity is `O(log(n/2))` where n is the input value ==> `O(log(n))`.

	The space taken by the algorithm is the same for any input value so `O(1)`
