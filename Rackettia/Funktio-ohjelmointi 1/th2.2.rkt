#lang racket
(define (average x y)
  (/ (+ x y) 2))

(define (make-point x y)
  (cons x y))

(define (x-point point)
  (car point))

(define (y-point point)
  (cdr point))

(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))

(print-point (make-point 3 5))

(define (make-segment a b)
  (cons a b))

(define (start-segment point)
  (car point))

(define (end-segment point)
  (cdr point))

(define (midpoint-segment segment)
  (cons (average (car (car segment)) (car (cdr segment))) (average (cdr (car segment)) (cdr (cdr segment)))))

(midpoint-segment (make-segment (make-point 1 1) (make-point 5 5)))