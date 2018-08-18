
a  = 9 
b = "9" 
c = concatenate(a, b)  // produces "99" 
d = add(a, b)          // produces 18 

# This is not possible in python as it is a strongly typed language.

a  = 9 
b = "9" 
c = concatenate(  str(a),  b)    // produces "99" 
d = add(a,  int(b)  )                //produces 18 