(defun belong(L)
	(cond 
		((or (eq L 'A) (eq L 'B) (eq L 'C)) T)
	)
)

(defun likes(L1 L2)
	(cond
		((and (eq L1 'A)(or (equal L2 "snow")(equal L2 "rain"))) t)
		((and (eq L1 'B) (not (likes 'A "snow")) (not (likes 'A "rain")))t)
		
	)
)

(defun mountain(L)
	(cond 
		((not (likes L "rain")) t)
	)
)

(defun skeir(L)
	(cond 
		((likes L "snow") t)
	)
)

(defun belongL(L)
	(cond
		((and (belong L) (mountain L) (not(skeir L))) T)
		
	)
)

(terpri)
(write "Check whether answer is A")
(print (belongL 'A))
(terpri)
(terpri)
(write "Check whether answer is B")
(print (belongL 'B))
(terpri)
(terpri)
(write "Check whether answer is C")
(print (belongL 'C))
(terpri)

