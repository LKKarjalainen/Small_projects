#lang racket
(require racket/trace)
(define (double x) (+ x x))
(define (halve x) (/ x 2))
(define (even? n)
  (= (remainder n 2) 0))

(define (fast-mult a b)
  (define (fast-mult-iter a counter product)
    (cond ((= counter 0) product)
          ((even? counter) (fast-mult-iter (double a) (halve counter) product))
          (else (fast-mult-iter a (- counter 1) (+ a product)))))
  (trace fast-mult-iter)
  (fast-mult-iter a b 0))

(fast-mult 7 0)