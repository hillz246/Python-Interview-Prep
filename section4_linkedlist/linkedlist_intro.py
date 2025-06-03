## Link Lists.
#This will be our first data structure.
#And then I'll go through and change this step by step to turn this into a linked list to highlight the differences between the two.

## So the first difference is that a linked list does not have indexes.
#a list is in a contiguous place in memory.


# these are all in a contiguous place in memory, this is why we can have indexes and access those indexes O of one, because we can map each one of these indexes to a specific address in memory.

### Linked List - Big O:

# ADDING: Head -> 11 3 23 7 -> Tail, adding 4 to end of list
# 
# This is O of one. O(1)
#The reason being, it doesn't matter how many nodes we have in the list, the number of operations to add it to the end is exactly the same.

# REMOVING: O(n): So we have to set it equal to another pointer. And the only thing that points to the seven node.

#So in order to get to that node, we have to start at the head, iterate through the list until we get to that pointer.
#Then we can set tail equal.
#To that pointer and that points it at the seven node.
# But because we had to iterate through the entire list, this is O of n.

# add an item to the front. O(1)
#We need to have that four point to the 11 node.
#The head points to the 11, so we'll have the next pointer from four be set equal.
#To head, and that points it at that node and that we have head point at the new node.
#And that adds it into the list.
#It doesn't matter how many items we have in the list, it's going to be the same number of operations
#to add an item on the front of the list.
#So that is O of one.

### removing that four node from front. O(1)
# The first thing we need to do is have head point at that 11 node.
# We can do that by saying head is equal to "head dot next".
#And that moves that over.
#And then we remove that item from the linked list.
#Once again this is going to be O of one because it doesn't matter how many items we have in the list,
#it's the same number of operations to remove that.

## adding an item somewhere in the middle of the list. O(n)
#we're going to insert that for after the 23 node.
#In order to find that node, we have to start at the head and iterate through the list until we get to that 23 node.
#Now we want the four to point at that seven node.
# And this pointer here is pointing at the seven.
# So we'll set the pointer from the four equal to that.
# We have that 23 node point to the new node. And that adds that into the linked list.
# But because we had to iterate through the list this is O of n.

### Removing four. O(n)
#We start at the head and we iterate through the list until we get to the four.
# We want the 23 to point at that seven node.
# So we're going to set the pointer from the 23 equal to the pointer that's going from the four to the seven.
# Then we can remove the four From the linked list.
#Once again we had to iterate through the list. This is O of n
#

#### linked lists under the hood. 
#NODE = the value and the pointer.
# it as a set of nested dictionaries and that is linked lists.