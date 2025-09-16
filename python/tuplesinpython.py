##empty tuple
#tuple1=()
#print(tuple1)

##tuple with int
#tuple1=(0,10,20,30)
#print(tuple1)

##tuple with mixed datatype
#tuple1=(100,'sahil',20000,'engg')
#print(tuple1)

##nested tuple
#tuple=("points",[10,10,20],(6,7,8))
#print(tuple)

##tuple can be created without parentheses () brackets
##also called tuple packing
#tuple=100,'sahil',20000,'engg'
#print(tuple)
##we can alos unpack a tuple below ex
#id,name,salary,dep = tuple
#print(id)
#print(name)
#print(salary)
#print(dep)
#
#print(type(tuple))


##accessing elements in tuple
#tuple = ('s','a','h','i','l')
#print(tuple)
#print(tuple[1])

##nested tuple
#tuple = ("point",[1,2,3],(4,5,6))
#          #we have a varaiable a list and tuple
#print(tuple)
#print(tuple[0][3])
#print(tuple[1][0])
#print(tuple[2][2])

##slicing tuple contents
#tuple = ('w','e','l','c','o','m','e')
#print(tuple[1:3])
#print(tuple[:-3])
#print(tuple[3:])
#print(tuple[:])

##tuple elements are immutable
#tuple = ('s','a','h','i','l')
#print(tuple)
##tuple[2]='x' #this will show error becouse we cannot update the content of the tuple
#   #we can reassing the value of a tuple
#tuple = ('s','a','h')
#print(tuple)


##concatenation of tuples
#tuple1 = ('wel')
#tuple2 = ('come')
#print(tuple1)
#print(tuple2)
#print(tuple1 + tuple2)
##reapting of tuples
#tuple3 = ('again',)
#print(tuple3*3)
#print(('again',)*4)

##deletion operation on a tuple
#tuple = ('w','e','l','c','o','m','e')
##as it is immutable so elements can not be deleted
#del tuple(2)
##but we can delete an entire tuple
#del tuple
#tuple = tuple
#print(tuple)

##tuple methods
#tuple = ('w','e','l','c','o','m','e')
#print(tuple.count('e'))
#print(tuple.index('c'))

#tuple operations
#tuple = ('w','e','l','c','o','m','e')

#membership
#print('c' in tuple)
#print('c'  not in tuple)
#print('a' in tuple)
#print('a'  not in tuple)

#if ('c' in tuple):
#       print('c' in tuple)

##iteration through tuple elements
#tuple = ('w','e','l','c','o','m','e')
#for i in tuple:
#    print("letter is ->",i)

##bulit in functions with tuple
#tuple = (1,2,3,4,5,7,8)
#
#print(max(tuple))
#print(min(tuple))
#print(sorted(tuple))
#print(len(tuple))