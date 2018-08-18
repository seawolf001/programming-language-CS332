
in  python 

1-	You must assign a value to a variable before you can use it, even if that value is zero or empty.
	
	for example, If I call the variable flag before assigning it a value:
	>>>flag

	I will get the following error:

	Traceback (most recent call last):
 	File "<stdin>", line 1, in <module>
	NameError: name 'Guido' is not defined

2-	Variable assignment works left to right.

	following are accepted :
	>>> flag = 0
	>>> flag = ""
	>>> flag = False

	following are  not accepted 
	>>> 0 = flag
	>>> ‘’ = flag
	>>> False = flag


The  Rules 

	1-   Variables names must start with a letter or an underscore, such as:
		_flag
    		flag_
    	2 -  The remainder of your variable name may consist of letters, numbers and underscores.
    		password1
    		n00b
		un_der_scores
	3 -  Names are case sensitive
		_flag_one , _FLAG_ONE, and _Flag_One are each a different variable.

	4 -  Class names should normally use the CapWords convention. 

	5 -  Because exceptions should be classes, the class naming convention applies here. 
	     However, you should use the suffix "Error" on your exception names (if the exception actually is an error). 

	6 -   Function names should be lowercase, with words separated by underscores as necessary to improve readability. 
	      # mixedCase is allowed only in contexts where that's already the prevailing style to retain
	      # The  Conventions to retain backwards compatibility.

	7 - Always use self for the first argument to instance methods. 

	8 - Constants are usually defined on a module level and written in all capital letters with underscores 
	    separating words. Examples include MAX_OVERFLOW and TOTAL 

The  Conventions :

	1 - Readability is very important. Which of the following is easiest to read? I’m hoping you’ll say the first example.
		python_puppet
		pythonpuppet 	
		pythonPuppet

	2 - Descriptive names are very useful. If you are writing a program that adds up all of the bad puns made in this book,
	    which do you think is the better variable name?

	    	total_bad_puns
    		super_bad

    	3 - Avoid using the lowercase letter ‘l’, uppercase ‘O’, and uppercase ‘I’. 
    	      	Why? Because the l and the I look a lot like each other and the number 1. And O looks a lot like 0.


python keyWords 

	False			lambda		global		not		with
	class 			try 		as 		elif		or
	finally			True		yield		assert		else
	is			def 		import 		pass 		break
	return			from 		except 		raise		in 
	None			nonlocal	while		continue	for  		and 		




