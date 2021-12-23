# Problem 6: Union and Intersection of Two Linked Lists

	
## Reasoning

# Union of Two Linked Lists

 	In order to solve the union of two linked lists, we exploit the property of removing duplicates
	of the pyhton's set structure.

	We simply go through each of the two linked lists and add each element to the set.
	once the set is built, we build a new linked list with the elements of this one

	go through the two linked lists takes each time `O(n)` where `n` is the number of the elements in one list.
	So `O(2n)` ==> `O(n)`.

	Fill in the new union linked list only takes `O(m)` where `m` is the number of unique elements in the set, 
	since we keep tracking the tail of the union linked list.

	The space requirements is linear since it depends on the number of unique elements. `O(n)` for the set and `O(n)` for the 
	union linked list ==> `O(2n)` ==> `O(n)`



# Intersection of Two Linked Lists

	In order to solve the intersection of two linked lists, we exploit pyhton's dictionary structure to keep tracking if
	an element belongs to the two linked lists.

	The idea is to fill the dictionary with the elements of the linked list as a key and initialize the value to `0` to check
	if the key has already been checked in the sencond linked list (to avoid duplication).

	We initialize the dictionary with the linked list containing the least elements, since potentially it will contain less 
	elements likely to be repeated in the second linked list (although that is not always true).

	Then, as we move forward in the second linked list, we append to the intersection linked list each element that exist in the 
	dictionary and it has not been 	added yet.

	Get the shortest linkend list is constant time since we track the size each time we add an element to this one.

	go through the two linked lists takes each time `O(n)` where `n` is the number of the elements in one list.
	So `O(2n)` ==> `O(n)`.

	The space requirements is linear since it depends on the number of unique elements in the dictionary and the number of unique 
	elements contained in the two lists . `O(n)` for the dictionary and `O(m)` for the intersection linked list 
	==> `O(n)+O(m)` ==> `O(n)` since we can not have more elements in the intersection linked list than in the dictionary.
	



 	

