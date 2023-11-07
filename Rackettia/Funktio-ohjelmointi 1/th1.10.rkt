#lang racket
(require racket/trace)
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1)
                 (A x (- y 1))))))
(trace A)

(define (tetration x y)
  (cond
    ((= y 1) (expt x y))
    (else (expt x (tetration x (- y 1))))))
    
  
(A 2 4)
(tetration 2 4)