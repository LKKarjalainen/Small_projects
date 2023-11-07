#lang racket
(define (inc n) (+ n 1))
(define (double-inc n) (+ n 2.0))
(define (square x) (* x x))
(define (product arg a next b)
  (if (> a b)
      1
      (* (arg a) (product arg (next a) next b))))
(define (factorial n)
  (product * 1 inc n))

(define (pi-term n)
  (if (even? n) 
       (/ (+ n 2) (+ n 1)) 
       (/ (+ n 1) (+ n 2))))

(define pi
  (* 4 (product pi-term 1.0 inc 1000.0)))

product
factorial
pi