#lang racket
(define (pTriangle depth width)
  (cond ((= depth 0) 1)
        ((= width 0) 1)
        ((= width depth) 1)
        (else (+ (pTriangle (- depth 1) width) (pTriangle (- depth 1) (- width 1))))))

(pTriangle 3 2)