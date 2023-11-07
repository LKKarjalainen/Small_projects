#lang racket

(define (accumulate combiner null-value term a next b)
  (if (> a b)
      null-value
      (combiner (term a) (accumulate combiner null-value term (next a) next b))))
(define (sum arg a next b)
  (accumulate + 0 arg a next b))
(define (product arg a next b)
  (accumulate * 1 arg a next b))

accumulate
sum
product