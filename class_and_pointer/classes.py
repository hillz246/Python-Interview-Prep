# Classes -> In coding, particularly in object-oriented programming (OOP), 
# a class is a blueprint or template for creating objects (specific instances of that class).

## def -> In programming—especially in Python—def is a keyword used to define a function.

#Python where you can create an integer, you can create strings.
#when you create a class you are creating your own data type.
#you want Python to do particular things. When you create a new cookie.
#And you do that with what is called a constructor and it has a particular syntax, it looks like this.

#a function with the def on there, And then it's double underscore init.
# one of the things that is going to be different about a method than a function is the ""self""" keyword.
#If it has self in there, it is a ""method that is part of a class""".

class Cookie:                               #class is Cookie
    def __init__(self,color):               # def = define a function, constructor __init__, self here is a method, parameter is color
        self.color = color   #self dot color applies to the specific instance of color that we're creating., = color is a variable
    
    def get_color(self):        # get_color(self)
        return self.color           #return self.color
    
    def set_color(self,color):      # set_color (self,value)
        self.color = color              #self.color = color


cookie_one = Cookie('brown')            # cookie_one is a variable name = integer/string here we use class
cookie_two = Cookie('grey')

print('cookie one is', cookie_one.get_color())
print('cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())


# class LinkedList:
#     def __init__(self,value):

#     def append(self, value):

#     def pop(self):

#     def pretend(self, value):

#     def insert(self, index, value):

#     def remove(self, index):




    

