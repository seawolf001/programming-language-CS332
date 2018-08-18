(defun increment (x L) 
	(if(null L) nil
		(cons (+ x (car L)) (increment x (cdr L)))
	)
)
(print "before")
(terpri)
(write '(1 2 3 4 5))
(terpri)
(print "after")
(terpri)
(write (increment 1 '(1 2 3 4 5)))

