#def a_void_function():
#    a=1
#    b=2
#    c=a+b
#    return(c)
#x=a_void_function()
#print(x)



#breaking
#for i in range(1,10):
#    if i == 5:
#        break
#    print(i)

#continue
#for i in range(1,10):
#    if i == 5:
#        continue
#    print(i)

##class 
#class glass:
#    def part1(parameters):
#        print("kya roll.....")
#    def part2(parameters):
#        print("kya bi nai")
#naam=glass()
#naam.part1()
#naam.part2()

##def
#def function_name(parameter):
#    pass     #(pass will not produce any output)
#function_name(10)

##del
#a = 10
#print(a)
#del a  #(after using del funtion a variable will get undefined)
#print(a)   #(so we will get an name error)

##if    elif   else
#num = int(input('any number '))
#print(type(num))   ## to know a type of an data we us type()
#
#if num == 1:
#    print('one')
#elif num == 2:
#    print('two')
#else:
#    print(num,'is something else')

##try  raise except finally
#try:          # lets you test a block of code for errors                   
#    x=9
#    raise ZeroDivisionError #raise Keyword is used to raise exceptions or errors
#except ZeroDivisionError:    #The except block lets you handle the error
#    print("division cannot be performed")
#finally:     #The finally block will be executed no matter if the try block raises an error or not
#    print("execution successfully")


##for
#for i in range(1,11):
#    print (i)

##from import
#import math
#from math import cos  #if we dont use this line we cann also use the below as follow
#print(cos(10))   #print(math.cos(10)) 


##global
#var=10
#def fun1():
#    print(var)
#def fun2():
#    global var
#    var=5
#def fun3():
#    global var
#    var=15
#def fun4():
#    print(var)
#fun1()
#fun2()
#fun1()
#fun3()
#fun1()
#fun4()


##in and not in
#a=[1,2,3,4,4]
#print(4 in a)   #it checks is the given data is in the list or not 
#print(1 not in a)

##is
#a=1
#b=1    #The test returns True if the two objects are the same object
#print(a is b)

##lambda
#a = lambda x: x*2
#for i in range(1,10): #lambda is a keyword in Python for defining the anonymous function
#    print(a(i))       #An anonymous function in Python is a function without a name. It can be immediately invoked or stored in a variable

##nonLocal
#def fun1():
#    a = 5
#    def fun2():
#        nonlocal a
#        a = 10
#        print("fun2 ",a)
#    fun2()
#    print("fun1 ",a)  
#fun1()
     #The nonlocal is a keyword in python that is used to declare any variable as not local but instead comes from the nearest enclosing scope that is not global.


##pass
#def function(args):
#    pass
     #pass is used to pass a function it is kept in case of use in future
      #it gives no output

##return
#def fun1():
#    a = 10
#    return a
#print(fun1())
   #A return statement is used to end the execution of the function call and “returns” the result to the caller

##while
#i = 5
#while(i>0):
#    print(i)
#    i -= 1
     #With the while loop we can execute a set of statements as long as a condition is true.

##with
#with open('example45.txt','w') as my_file:
#    my_file.write('hello world')
    #In Python, with statement is used in exception handling to make the code cleaner and much more readable
   #"open"it opens a file for you so you can work with the file.


##yield
#def generator():
#    for i in range(6):
#        yield i*i
#        
#g = generator()
#for i in g:
#    print(i)

#(It allows a function to produce a sequence of results over time,
# rather than calculating them all at once and returning them in a 
#list. This makes it incredibly memory-efficient, especially when dealing
# with large sequences of data.)
