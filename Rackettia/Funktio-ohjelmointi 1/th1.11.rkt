#lang racket
(define (prc n)
  (cond ((< n 3) n)
        (else (+ (prc (- n 1)) (* 2 (prc (- n 2))) (* 3 (prc (- n 3)))))))


(define (prd n)
  (define (f-loop n1 n2 n3 stop)
    (cond ((= n stop) n1)
          (else (f-loop (+ n1 (* 2 n2) (* 3 n3)) n1 n2 (+ 1 stop)))))
  (cond ((< n 3) n)
      (else (f-loop 2 1 0 2))))
      
(prc 3)
(prd 3)