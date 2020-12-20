#!/usr/bin/env python3
squares = [1, 1, 'four', 9, 9, 9, 16, 25] #making list
print(squares)
print(squares[2]+' '+str(squares[3]))

squares[1] = 4 #replacing an element by index
print(squares)
print(len(squares)) #length of list
print(squares.count(9)) #counting an element

del squares[2] #deleting an element
print(squares)
print(len(squares))
squares.append('syou') #appending(adding) an element
print(squares)
print(len(squares))
squares.remove(9) #removing an element
print(squares)
print(len(squares))
squares.insert(3,2) #inserting an element by index
print(squares)
print(len(squares))
squares.pop(2) #popping an element by index
squares.pop()
print(squares)
print(len(squares))
squares.reverse() #reversing elements
print(squares)
squares.sort() #sorting elements
print(squares)
squares.clear() #emptying all
print(squares)
print(len(squares))
