## example of "O of n"
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

## example of "O of 2n simplify O(2n) "dropping constant" o(n)"
## DROP CONSTANT O(n)

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)

## for loop inside the for loop, n*n = n2 n square, O of n squared, O(n2+n) 
## O (n2) - less efficient from a time complexity standpoint.

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)

## Drop Non-dominants
## O (n2 ) + O(n) -> drop O(n) -> have O(n2) 

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i)
    for k in range(n):
        print(k)
print_items(10)

## O of 1:
# O(1) : It's the most efficient big O.


## even if we have two additions like we do here, the number of operations will remain constant as n increases.
#Of one is just that flat purple line across the bottom is just going to stay across the bottom because as it increases, we are not increasing the number of operations.


## "n of log N":

# 2 to the third power is 8 -> 2 3 = 8 -> log2 8=3
# log2 1,073,741,824 = 31, to get this big number you devide by 2 how many times? is 31  

#And that is the power of O of log n.
#So now let's take a look at this on the graph.
#You can see that it is very flat, very efficient.
#Not as flat as O of one, of course, but it is far more efficient than O of n or O of n squared.
#So these four are going to be what we see for most of the course.


## O(nlog n) 
# " O of n times log n"    -> that is used with some sorting algorithms."
# And this is the most efficient that you can make a sorting algorithm.
# you're going to sort various types of data, you're going to sort strings.


# Different terms for inputs is a big O concept
# O(a+b)

def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(b)

# O(a*b)

def print_items(a):
    for i in range(a):
        for j in range(b):
            print(a,b)


## Big O of list 
# 11,3,23,7
# 0 1 2 3

# my_list.append(17)
# 11,3,23,7,17
# 0 1 2 3 4

## my_list.pop(17)
# 11,3,23,7, 17
# 0 1 2 3   4 

# O(1) are two things above
#Once again, when we remove that, there is no reindexing all the way down the line.
#All we have to do is add or remove when we do an append or a pop.
#So that is O of one.

# my_list.pop(0)
#pop at the index of 0, 

# 11,3,23,7
# 0 1 2 3
# When we remove this, the problem that we have is that this index is now incorrect.
# So we need to take that index of one and re-index it to a zero
# 3,23,7
# 0 1 2
# mylist_insert(0,11)
# 11,3,23,7
# 0 1 2 3
# in this above case So it doesn't matter if you're removing or if you're adding to a list.
#It's O of N and in in this case is the number of items in the list.
#""O(n)"" is insert above


#""Important thing to remember"""
#right side end adding/removing is O(1), e.g. 17
#left side removing number - need reindexing has to happend and adding - is O(n), e.g. 11

## if we add in middle
# 11,3,23,7
# 0 1 2 3
#insert 'Hi' - need reindexing is O(n)
## 11,Hi,3,23,7
##  0 1 2 3 4
# same thing remove 'Hi' - need reindexing is O(n)
# 11,3,23,7
# 0 1 2 3

# if n=100, O(1) = 1, O(log n)=7, O(n)= 100, O(n2) = 10,000 (O of square is big number - inefficient)
# if n=1000, O(1) = 1, O(log n)=10, O(n)= 1000, O(n2) = 1,000,000 (n squared is million - growing very fast)

# So we'll see as we get into the course, there will be situations where you do something and it's O of n squared.
#And you can rewrite the code and make it O of n.
#That is a huge increase in efficiency when you can do that.

#### terminology for all of these. ####

# O of n squared is a loop within a loop.
#O of N is proportional, it will always be a straight line.
# O of log n. Divide and conquer.

## IMPORTANT: When you hear that that is O of log n and o of one is constant time.

#So those are our four terms for our four big O's that we'll see for most of the course.
#O(1) - Excellent/Best, O(log n) - Good, O(n) - Fair, O(n log n) - Bad, O(n^2), O(2^n) and O(n!) - Horrible/Worst
