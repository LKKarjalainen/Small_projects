#lang racket
; Your function here...
(define (double f)
  (lambda (x)(f (f x))))

; A function that applies your function, for exercise checker.
(define (applier f x)
    ((double f) x))

; So that the exercise checker knows which function to check
applier