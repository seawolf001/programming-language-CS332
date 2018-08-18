(defun factorial (n)
  (if (= n 0) 1
      (* n (factorial (- n 1))) 
  ) 
)
(write "enter the  number : ")
(terpri)
(format t "factorial of given number is  :  ~D"(factorial(read)))
