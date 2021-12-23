# Problem 4: Active Directory

	For this problem, the goal is to write code that provides an efficient look up of whether the user is in a group

## Reasoning

 	The problem can be solved by recursively iterating through each group and its subgroups.
	
	If the user is in the group itself the function returns true.

	Else, we call the function recursively until we find the user in one of the subgroups belonging to this group and then
	return true or until all the subgroups belonging to this groups are checked without positive results and then return false.

	Insofar as no assumption is made concerning the possibility of a circular dependency between groups , we mark each visiting
	group in order to avoid an infinite loop or repetition.

## Time complexity

	Since each group is scanned only once, the time would be proportional to the number of groups and users scanned.

	So if `n` is the number of groups and `m` is the number of users, the running time will be linear `O(n+m)` ==> `O(n)`



## Space complexity

	The space complexity is determined by the recursion depth of the scanned group. 

	So, if `n` is the number of subgroups, the space complexity will be linear `O(n)`
