(defun memberList(X L)
( 
	cond
		((null L) nil)
		((equal X (car L)) t)
		(t (memberList X (cdr L)))
)
) 	
(write (memberList 10 '(1 2 3 4)))
(terpri)
(write (memberList '(1) '((1) 2 3 4)))
(terpri)
(write (memberList 2 '(1 2 3 4)))
