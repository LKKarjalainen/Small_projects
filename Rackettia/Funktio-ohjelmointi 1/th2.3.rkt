#lang racket

(define (diff x y)
  (cond
    ((< x y) (- y x))
    ((< y x) (- x y))
    (else 0)))

(define (make-point x y)
  (cons x y))

(define (make-segment a b)
  (cons a b))

(define (segment-len seg)
  (+ (diff (car (car seg)) (car (cdr seg))) (diff (cdr (car seg)) (cdr (cdr seg)))))

;; (segment-len (make-segment (make-point 0 1) (make-point 0 6)))

;; Rectangle from points
(define (point-segment-rectangle a b c d)
  (cons (cons (make-segment a b) (make-segment b c)) (cons (make-segment c d) (make-segment d a))))
(point-segment-rectangle (make-point 0 0) (make-point 0 5) (make-point 5 5) (make-point 0 5))

;; Rectangle from segments
(define (segment-rectangle a b c d)
  (cons (cons a b) (cons c d)))
(segment-rectangle (make-segment (make-point 0 0) (make-point 0 5)) (make-segment (make-point 0 5) (make-point 5 5)) (make-segment(make-point 5 5) (make-point 5 0)) (make-segment(make-point 5 0) (make-point 0 0)))

(define (rect-perim rectangle)
  (+ (segment-len (car (car rectangle))) (segment-len (car (cdr rectangle))) (segment-len (cdr (car rectangle))) (segment-len (cdr (cdr rectangle)))))

(rect-perim (point-segment-rectangle (make-point 0 0) (make-point 0 5) (make-point 5 5) (make-point 0 5)))
(rect-perim (segment-rectangle (make-segment (make-point 0 0) (make-point 0 5)) (make-segment (make-point 0 5) (make-point 5 5)) (make-segment(make-point 5 5) (make-point 5 0)) (make-segment(make-point 5 0) (make-point 0 0))))

(define (rect-area rectangle)
  (* (segment-len (car (car rectangle))) (segment-len (car (cdr rectangle)))))

(rect-area (point-segment-rectangle (make-point 0 0) (make-point 0 5) (make-point 5 5) (make-point 0 5)))
(rect-area (segment-rectangle (make-segment (make-point 0 0) (make-point 0 5)) (make-segment (make-point 0 5) (make-point 5 5)) (make-segment(make-point 5 5) (make-point 5 0)) (make-segment(make-point 5 0) (make-point 0 0))))