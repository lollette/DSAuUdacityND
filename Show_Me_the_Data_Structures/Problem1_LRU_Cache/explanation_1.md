# Problem 1: LRU Cache

	LRU caches store items in order from most-recently used to least-recently used. 
	That means the most-recently used item can be accessed in O(1) time. 

	Also, it lets us update the cache in O(1) time so that the cache is always ordered.

	Finally, since the cache has a limited capacity, the LRU is an efficient cache data 
	structure that can be used to figure out what we should evict when the cache is full.
	The goal is to always evict the least-recently used item in O(1) time. 


## Reasoning

	1**/ To allow the addition of new items at the beginning of the list, changing the location of an 
	already existing item to the beginning of this one or deleting the item at the end of the list 
	in constant time, I opted for double linked lists as one of the two basic data structures used for my LRU, 
	with the most-recently used item at the head of the list and the least-recently used item at the tail.

	This lets me:
		- access the first LRU item in O(1) time by looking at the head of the list 
		- remove the last LRU item in O(1) time by looking at the tail of the list 
		- add a new item to the cache by prepending it to the beginning of the list in O(1) 
		- bring back an already existing item at the beginning of the list in O(1) time 


	2**/ In general, finding an item in a double linked list is O(n) time, since we need to walk the whole list. 
	     But the whole point of a cache is to get quick lookups. So the second structure used here is 
	     a hashmap that maps items to double linked list nodes and lets me find an item in the cache's double linked 
	     list in O(1) time, instead of O(n). In this implementation the hashmap is a python dictionary. 



	3**/ As I mentioned above, the cache has a limited capacity. So each time an item has to be added in the cache
	     we have to check that the capacity of this one is not reached yet.
	     If so we must first delete the least-recently used item before adding the new item.
	     For that I added a variable to track if the cache capacity is reached.


## Working
	
	1**/ set() function:

	     Adding an item to the cache is done by using the set() function. 
	     
	     The latter takes as arguments the value of the item as well as the corresponding key.
	     
      	     Whenever an item needs to be added to the cache, the function checks whether the key already exists or not.
	
	     If the key exists the function deletes the corresponding node from its current location and adds a new node at the top
	     of the list.

	    If on the other hand, the key does not exist, the function first checks if the maximum capacity is reached. If so, it
	    will first proceed to the removal of the least-recently used item and then add the new one. Otherwise it will 
   	    add the item directly and then increment the value of the current cache size.


	2**/ get() function:

	     Getting an item from the cache is done by using the get() function.

	     The latter takes as argument the corresponding key of the desired item then checks if this one is in the hash map.
	     If the key exists the function deletes the corresponding node from its current location and prepends it at the top
	     of the list then return the node value otherwise the function return -1.



## Space analysis


	An LRU cache tracking n items requires a double linked list of length n, and a hashmap holding n items. 
       	So space Complexity will be O(n).
