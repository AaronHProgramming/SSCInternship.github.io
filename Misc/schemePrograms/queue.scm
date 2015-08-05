;(define make-queue 
;  (let ((front-ptr '())
;        (back-ptr '()))
;    de
;    (define (dispatch m)
;    dispatch))

(define (full-queue queue) (car queue))
(define (back-ptr queue) (cdr queue))
(define (set-queue! queue item) (set-car! queue item))
(define (set-back-ptr! queue item) (set-cdr! queue item))
(define (empty-queue? queue) (null? (front-ptr queue)))
(define (peek-front-of-queue queue)
  (if (empty-queue? queue) (error "No front value of an empty queue") (car (full-queue queue))))
(define (insert-queue queue item) 
  (let ((new-pair (cons item '())))
    (if (empty-queue? queue) ((set-queue! queue new-pair) (set-back-ptr! queue new-pair)(set-cdr! (cons queue (item
(define (dequeue queue) 
(define queue make-queue)
(car queue)
