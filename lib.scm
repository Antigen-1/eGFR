(define pow (#%vm-procedure (=> (dynamic-require "builtins" none) "pow") 2))
(define <= (#%vm-procedure (=> (dynamic-require "operator" none) "le") 2))
(define >= (#%vm-procedure (=> (dynamic-require "operator" none) "ge") 2))

(define min (lambda (n1 n2) (if (< n1 n2) n1 n2)))
(define max (lambda (n1 n2) (if (< n1 n2) n2 n1)))