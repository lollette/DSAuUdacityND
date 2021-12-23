# Problem 7: HTTPRouter using a Trie


## Reasoning

	Inserting and finding a path requires both `O(n)` where `n` is the number of component parts of the path.

	Both ` add_handler()` and `lookup()` call `split_path()` to first split the path  into parts ==> 
	`O(c)` time where `c` is the number characters in the path and 
	returns them as a list ==> `O(n)` time where `n` is the number of component parts of the path.

	Space complexity is determined by the number of component parts of the path and the space related to saving the handlers.
