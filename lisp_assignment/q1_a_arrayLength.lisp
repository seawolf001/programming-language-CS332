(defun arrayLength(arr)
	(cond 
		((null arr) 0)
		(T (+ 1 (arrayLength (cdr arr))))
	)
)
(terpri)
(format t "Length of the array is : ~D"(arrayLength '(1 (2 6) 3 4 5)))