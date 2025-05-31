# pointers = In programming, a pointer is a variable that stores the memory address of another variable.
# Think of it like a signpost that points to where a value is stored in memory.

num1 = 11

num2 = num1

print('before num2 value is updated:')
print('num1=', num1)
print('num2', num2)

print('\nnum1 points to:', id(num1))        # id gives the address where num1 is stored
print('num2 points to:', id(num2))

num2 = 22

print('\nafter num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)


print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))


## can point number one to a different integer that is stored somewhere else, which you can't actually change the number 11 once you create it.


dict1 = {
         'value': 11
}
dict2 = dict1


print('Before value is updated:')
print('dict =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))

dict2['value'] = 22

print('\nAfter value is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))

## So with dictionaries we can take that number 11 and then change it to a 22 where ""integers are immutable""" and can't be changed.

## Dictionaries can be changed.##

## So dictionary one and dictionary two continue pointing to the same place, but we are able to change the value.

## For example, when we have a linked list, the nodes in a linked list are going to operate very much like a dictionary.
#So if you have two variables that point at the same node, you can change the value of that node.
#Say we change this from a 22 to a 44.
#Say the variables continue to point at the same node even though we changed the value.

# And then there's another concept I want to explain.

#And to do that I'm going to set dictionary one to be equal to dictionary two.
#And we'll have all three variables pointing at this same dictionary.
#Now the question is what happens to this dictionary because we no longer have anything pointing to it.
#And if you don't have a variable that's pointing to this, you don't have any way to access this.

#So what Python does in this situation is Python will remove this through a process called garbage collection.