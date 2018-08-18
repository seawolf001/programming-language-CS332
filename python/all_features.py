# import time ;

#object-oriented
class compute:
	def __init__(self):
		print ("")

	def comp_add(self,x,y): #functional
		print("-------------------------------------------------")
		print ("calculated using functional programing paradigm")
		print("-------------------------------------------------")
		return ( x + y )

	def sum_fifty(self):
		print("-------------------------------------------------")
		print ("Demonstrating Reflective programing paradigm")
		print("-------------------------------------------------")
		ans=0
		for i in range(50):
			ans += i
		print ("the sum from 1 to 50 is", ans)

	def add_list(self,Mylist):#procedural
		print("-------------------------------------------------")
		print("Demonstrating procedural programing paradigm")
		print("-------------------------------------------------")
		print("Sum of  the  element  in the  list : ")
		ans=0
		if type(Mylist) is list:
			for x in Mylist:
				ans+=x
		return ans

print("*************************")
print ("Python Program Started")
print("*************************")	
# print time.localtime(time.time())
comp = compute()
sum_1_2 = comp.comp_add(1,2)
print("sum of 1 and 2 is : ")
print (sum_1_2)
l = [1, 2, 3]
print(comp.add_list(l))

print("---------------------------------------------------")
print("Demonstrating use of set in python")
SET = set([1,1,2,2,3,4,5])
print SET
print("---------------------------------------------------")

print("---------------------------------------------------")
print("Demonstrating use of frozenset in python")
a = frozenset([1,2,3])
b = frozenset([2,3,4])
c = a.union(b)
print c

print("---------------------------------------------------")
print("---------------------------------------------------")
print ("Demonstrating use   of list  in python")
MYLIST = [1,2,3,4,5,6,7,8,9]
print MYLIST
print("---------------------------------------------------")

print("---------------------------------------------------")
print("Demonstrating use  of string in python")
text = 'My name is  jitendra kumar'
print text[0]
print text[8]
print "44".isdigit()
print "44".isalpha()
print "44".isupper()
print "AA".isupper()
print "aa".islower()
print("---------------------------------------------------")
print("---------------------------------------------------")
print("Demostrating use of tuples in python")
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0] : ", tup1[0])
print ("tup2[1:5] : " ,tup2[1:5])
print("---------------------------------------------------")
print("---------------------------------------------------")
print ("Demonstrating  use of dictionary in python")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
print("---------------------------------------------------")


def fact_recur(z):		#recursion
	if(z==0):
		return 1
	return z*(fact_recur(z-1))

def fact_iter_for(z):
	ans=1;
	for y in range(z):
		ans = ans *(y+1)
	return ans
def fact_iter_while(z):
	ans=1;
	while(z > 1):
		ans = ans * z
		z= z-1
	return ans
print("-------------------------------------------------")
print("demonstrating recursion")
print("-------------------------------------------------")
print("factorial of 5 is :")
print(fact_recur(5))
print("-------------------------------------------------")

class_name = "compute"
method = "sum_fifty"
obj = globals()[class_name]()
getattr(obj,method)()

print("\n\n\n")

print("-------------------------------------------------")
print ("Demonstrating Strongly Typed")
print("-------------------------------------------------")	
#strongly typed
try:
	_hello = "hello" + 5 + goodbye
	print (_hello)
except:
	print ("error due to strongly typed")
print("\n\n\n")

#dynamically typed
print("-------------------------------------------------")
print ("Demonstrating dynamically typed")
print("-------------------------------------------------")
_hello = "hello python"
print ("Type of varibale _hello is : ",type(_hello))
_hello = 5
print ("Now Type of varibale _hello is : ",type(_hello))

print("\n\n\n")

#duck typing 
print("-------------------------------------------------")
print ("Demonstrating duck typing")
print("-------------------------------------------------")
_hello += 10
print (_hello)

_hello = float(_hello)
print ("Now Type of varibale _hello after type casting is : ",type(_hello))


print("-------------------------------------------------")
print ("Demonstrating recursion")
print("-------------------------------------------------")	
print ("factorial by recursion ",fact_recur(5))
print("\n\n\n")

print("-------------------------------------------------")
print ("Demonstrating Iteration using For Loop")
print("-------------------------------------------------")	
print ("factorial by iteration for loop", fact_iter_for(6))
print("\n\n\n")


print("-------------------------------------------------")
print ("Demonstrating Iteration using While Loop")
print("-------------------------------------------------")	
print ("factorial by iteration while loop", fact_iter_while(7))
print("\n\n\n")

