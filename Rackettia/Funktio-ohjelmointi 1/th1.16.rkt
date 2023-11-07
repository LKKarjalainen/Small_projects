#lang racket
(require racket/trace)
(define (square x) (* x x))
(define (even? n)
  (= (remainder n 2) 0))

(define (expt-iter b n)
  (iter-expt b n 1))

(define (iter-expt b counter product)
  (cond ((= counter 0) product)
        ((even? counter) (iter-expt (square b) (/ counter 2) product))
        (else (iter-expt b (- counter 1) (* b product)))))

(trace iter-expt)
(iter-expt 2 1 1)
(expt 2 1)