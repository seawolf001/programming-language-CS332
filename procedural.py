class compute:
	def __init__(self):
		print ("")

	def add_list(self,Mylist):
		print ("\nDemonstrating procedural python programming")
		print ("---------------------------------------------")
		print("Sum of  the  element  in the  list : ")
		ans=0
		if type(mylist) is list:
			for x in mylist:
				ans+=x
		return ans
obj = compute()
mylist = [1, 2, 3]
print(obj.add_list(mylist))
