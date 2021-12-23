# Problem 5: Autocomplete with Tries


## Reasoning

	Inserting and finding a word requires both `O(n)` where `n` is the number of characters in the word.

	Constructing a whole trie depends directly on how many words the trie contains, and how long those words could 
	potentially be. So, the worst-case runtime for creating a trie is a combination of `n`, the length of the longest word
	in the trie and `w`, the total number of the words to insert. Thus, the worst case runtime of creating a trie is  `O(w*n)`
	==> `O(wn)`.

	Same logic for space required to strore the whole Trie ==> `O(wn)`.


	The time complexity of listing all suffixes that exist below the prefix that is being searched for in the trie
	depends on the length of the longest suffixe `n` and the number of total words sharing this prefix `w`, making the 
	runtime of these operations also `O(wn)`


	Once again, Same logic for space required `O(wn)`, since in the worst case we have to go through the whole trie.
	So, the space is determined by the recursion depth which will be equal to the longest word in the trie and the number of 	 total words sharing the prefix. Adding to this the space allocated to store the suffixes found `O(wn)` 
	==> `O(2wn)` ==> `O(2wn)`


	Basically, we can sum it all up by saying that in the worst case, time and space depend on the sum of the characters of all 		the words.
	
