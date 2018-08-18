class compute:
	def __init__(self):
		print ("")

	def comp_product(self,x,y): #functional
		print("-------------------------------------------------")
		print ("calculated using functional programing paradigm")
		print("-------------------------------------------------")
		return ( x * y )

obj = compute()
product  = obj.comp_product(4,5)
print product
