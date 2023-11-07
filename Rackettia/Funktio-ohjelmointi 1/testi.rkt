#lang racket
(displayln "Hello, World!")

(define (add x y)
  (+ x y))

(define (summa lista)
  (define sum 0)
  (for ([i lista])
    (set! sum (add sum i))))

(displayln (add 5 3))
(displayln (add (add 5 3) 3))

(define my-list '(1 2 3 4 5))
(for ([i my-list])
  (displayln i))
(displayln (summa my-list))
(define string-list '("bro" "bruh"))
(for ([s string-list])
  (displayln s))
