# Reverse-Polish-Notation(RPN) Solver

This program evaluates [Reverse-Polish notation(RPN)](https://en.wikipedia.org/wiki/Reverse_Polish_notation) in a spreadsheet. For purposes of this program a spreadsheet is defined as two-dimensional array of cells, labeled A1, A2, etc. Rows are
identified using letters, columns by numbers. Each cell contains either an integer (its value) or
an expression. Expressions contain integers, cell references, and the operators ‘+’, ‘-’, ‘*’, ‘/’ with
the usual rules of evaluation - note that the input is RPN and should be evaluated in stack order.


## Input
3 2
A2
4 5 *
A1
A1 B2 / 2 +
3
39 B1 B2 * /

## Output
3 2
20.00000
20.00000
20.00000
8.66667
3.00000
1.50000