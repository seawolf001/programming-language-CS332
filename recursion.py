
def fact_recur(z):		#recursion
	if(z==0):
		return 1
	return z*(fact_recur(z-1))

print("demonstrating recursion\n")
print("factorial of 5 is :" , fact_recur(5))
