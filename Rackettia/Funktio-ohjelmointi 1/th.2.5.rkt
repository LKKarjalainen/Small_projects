#lang racket
(define (cons a b)
  (* (expt 2 a) (expt 3 b)))

(define (car z)
  (define (car-loop z counter)
    (if (= (modulo z 2) 0) (car-loop (/ z 2) (+ counter 1))
        counter))
  (car-loop z 0))

(define (cdr z)
  (define (cdr-loop z counter)
    (if (= (modulo z 3) 0) (cdr-loop (/ z 3) (+ counter 1))
        counter))
  (cdr-loop z 0))
(cons 1 1)
(cons 3 3)
(car (cons 6 5))
(cdr (cons 7 8))