# Problem 3: Huffman Coding

## Reasoning

	In order to build the tree, we first estimate the frequencies of occurrence of each character using a dictionary.
	
	This will take `O(n)` time where `n` is the size of the original input string and `O(m)` space where `m` is
	the number of unique characters.


	Then, we build the tree using a minheap based priority queue to enable a an efficient sorting and eviction of the lowest
	frequency.

	The initialization of the priority queue takes `O(nlog(n))` where `n` is the number of unique characters.

	The construction of the tree consists of recovering the two nodes whose frequencies are the lowest, combining them in a
 	new parent node whose frequency will be equal to the sum of these two nodes and then inserting this parent node back into
	the priority queue which takes `O(log(n))`.

	We repeat this step until only one node remains in the priority queue. So, in the worst case which is the case where 
	the text contains only unique characters, building the Huffman tree takes `O(nlog(n))` where `n` is the number of unique 
	characters and requires linear `O(n)` storage space.

	Once the tree is built, we map each character to its code using a dictionary. This step requires to traverse the whole
	tree which takes `O(n)` with `n` is the numbers of nodes in the tree. However, the advantage of this step is that it 
	allows us to avoid traversing the whole tree for each character. Instead we will simply search for the character in the 
	dictionary and retrieve the corresponding code in `O(1)`. 

	The space complexity for this dictionary is the same as the frequencies one which is `O(m)` where `m` is the number of 
	unique characters.


	The decoding of the binary sequence to its original form is done by moving from one node to the next one according to the code 
	until reaching the node containing the character. Each time a character is found we restart from the root node.
	
	The deconding step depends on the size of the binary sequence, so it takes `O(n)` where `n` is the number of bit constituting the 
	binary sequence.




