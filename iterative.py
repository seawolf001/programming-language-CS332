
def fact_iter_while(z):
	ans=1;
	while(z > 1):
		ans = ans * z
		z= z-1
	return ans

print ("Demonstrating Iteration using For Loop\n")
print ("factorial by iteration while loop", fact_iter_while(6))
