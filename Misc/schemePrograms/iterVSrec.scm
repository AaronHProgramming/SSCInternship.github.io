(define (rec-factorial x)
  (if (= x 0) 1 (* x (rec-factorial (- x 1)))))

(define (iter-factorial-helper product counter max-count)
  (if (> counter max-count)
      product
      (iter-factorial-helper (* product counter) (+ counter 1) max-count)))

(define (iter-factorial x) (iter-factorial-helper 1 1 x))

(newline)
;(define t (current-seconds))
;(rec-factorial 41875)
(rec-factorial 999)
(newline)
;(display (- (current-seconds) t))
(newline)
;(define t (current-seconds))
;(iter-factorial 100000)
(newline)
;(display (- (current-seconds) t))
(display "Success")
