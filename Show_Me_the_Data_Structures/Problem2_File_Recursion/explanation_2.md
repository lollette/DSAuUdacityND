# Problem 2: File Recursion

	For this problem, the goal is to write code for finding all files under a directory 
	(and all directories beneath it) that end with a specific suffix

## Reasoning

 	The problem can be solved by recursively iterating through all the items contained in the 
	parent folder and its subfolders at different levels.

	If the item is a file and its suffix matches the searched suffix, we add its path to the list of files to return.

	If, on the other hand, the item is a folder we call the function recursively until we have scanned all the files.

## Time complexity

	Since each item is scanned only once, the time would be proportional to the number of items scanned.

	So if `n` is the number of items in the parent folder and its subfolders at different levels,
	the running time will be linear `O(n)`



## Space complexity

	The space complexity is determined by the recursion depth and the number of files found. 

	So same as above, if `n` is the number of items in the parent folder and its subfolders at different levels
	and `m` the returned list size, the space complexity will be linear `O(n + m)` ==> `O(n)`
