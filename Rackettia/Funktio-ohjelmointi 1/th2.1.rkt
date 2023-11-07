#lang racket
(define (make-rat n d)
  (let ((g (gcd n d)))
    (if (negative? d)
        (cons (/ (* n -1) g) (/ (* d -1) g))
        (cons (/ n g) (/ d g)))))

(make-rat -5 -10)