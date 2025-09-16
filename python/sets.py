##sets
##sets of integer
#set1={11,33,66,55,44,22}
#print(set1)

##set of mixed datatypes
#set2={101,"sahil",(21,2,119)}
#print(set2)

##duplicate values are not allowed
#set3={11,33,66,55,44,22,11,33,44}
#print(set3)

##set cannot have mutable items (error in output) if we put list in set
#set4={1,2,[1,2]}
#print(set4)

##we can make set from a list
#set5 = set([1,2,3,4])
#print(set5)
#print(type(set5))

##we can make list from set
#list1=list({1,2,3,4})
#print(list1)
#print(type(list1))

##operation on sets set elements are printed randomly
#sets={11,2,3,4,5,7} #Unlike lists, ordinary sets do not
#print(sets)         #preserve the order in which we insert the element
                     #This is because the elements in a set are usually 
                     #not stored in the order in which they appear

##set does not support indexing
##means we cannot call the elements of the set
#sets={11,2,3,4,5,7}
#print(sets(0))
#sets(0)
#print(sets)

##add an element
#sets={11,2,3,4,5,7}
#sets.add(77)
#print(sets)

##add multiple elements we use update
#sets={11,2,3,4,5,7}
#sets.update([77,33,4,6,7,7])
#print(sets)

##we can add list and set also in sets
#sets={11,2,3,4,5,7}
#sets.update([77,33,4,6,7,7],{54,765,234})
#print(sets)

## remove and discard
#sets={11,22,33,44,66,55}
#print(sets)
##discarding an element whuch is not present will not make an errror
#sets.discard(4)
#print(sets)
##removing and element which is not present will make an error
#sets.remove(5)
#print(sets)
##discarding and removing of a element which is present can be done
#sets.discard(44)
#sets.remove(55)
#print(sets)

##using pop
#sets={11,22,33,44,66,55}
#print(sets)

##we can pop an random element multiple times
##pop can be used will printing statement or outside
#sets.pop()  #this will pop an element 
#print(sets.pop())  #but this show which element is getting poped
##sets.pop(11) #this will make an error sets.pop will take no args
#print(sets)

##clear my set
#sets.clear() ## this will clear an entire set
#print(sets)


##set operations union
#set1={0,1,2,3,4,5}
#set2={6,7,5,8,8,9,10}
#
#print(set1.union(set2))
#print(set1 | set2)

##set operations intersection means it will show the common elements
#set1={0,1,2,3,4,5}
#set2={6,7,5,8,8,9,10}
# #it will show the common elements from both sets
#print(set1.intersection(set2))
#print(set1&(set2))

##set opertions - set difference
#set1={0,1,2,3,4,5}
#set2={6,7,5,8,8,9,10}
#  
#print(set1 - set2) #this will remove the common element from set one {0, 1, 2, 3, 4} 
#print(set2 - set1) #{6, 7, 8, 9, 10}
#print(set2.difference(set1))
#print(set1.difference(set2))

##set opertions - symmetric differece
#set1={0,1,2,3,4,5}
#set2={6,7,5,8,8,9,10}
#   ##in this the common elements will not appear but both sets will come
#print(set1 ^ set2)
#print(set2 ^ set1)
#print(set2.symmetric_difference(set1))
#print(set1.symmetric_difference(set2))

##frozenset
 #these have the charactersitcs just like set but they are
 # immutable just like tuples
#set1 =  frozenset([1,2,3,4])
#set2 =  frozenset([3,4,5,6])
#print(set1)
#print(set2)
#print(set1 | set2)
#print(set1 & set2)
#print(set1 - set2)
#print(set1 ^ set2)
