Title: Fibonacciho posloupnost
Date: 2015-05-07 16:47
Category: úloha
Tags: mírně pokročilý, podmínky a cykly, rekurze, funkce
Author: Marek Nožka


[Fibonacciho posloupnost](https://cs.wikipedia.org/wiki/Fibonacciho_posloupnost)
je dána předpisem: 

$$
 F(n)=
  \left\\{
   \begin{matrix}
    0\,,\qquad\qquad\qquad\quad\,\ \ \,&&\mbox{pro }n=0\,;\ \ \\\\
    1,\qquad\qquad\qquad\qquad\,&&\mbox{pro }n=1;\ \ \,\\\\
    F(n-1)+F(n-2)&&\mbox{pro }n>1
   \end{matrix}
  \right.
$$

Jednoduše řečeno: každý další člen posloupnosti je součtem předchozích dvou členů.

# 1. Program

Vytvořte program, který na obrazovku vytiskne prvních N členů 
[Fibonacciho posloupnosti](http://cs.wikipedia.org/wiki/Fibonacciho_posloupnost).


## Příklad komunikace programu: 

    Zadej počet členů: 9
    >>> 0, 1, 1, 2, 3, 5, 8, 13, 21

# 2. Funkce

Svůj původní program předělejte: vytvořte funkci, která bude vracet
*n-tý* člen fibonacciho posloupnosti.

    :::python
    def fib(n):
        if n = 0:
            return 0
        elif n ...
        ...
     ...

    print(fib(5))

# 3. Rekurze

Opět vytvořte funkci, která vrací *n-tý* člen fibonacciho posloupnosti, ale 
tentokrát s využitím [rekurze]().

[rekurze]: https://cs.wikipedia.org/wiki/Rekurze

    :::python
    def fibR(n):
        ...
        return fibR(n-2) + fibR(n-1)
        ...

Porovnejte rychlosti výpočtu:

    :::python
    print(fib(36))
    print(fibR(36))

# 4. Generátor a iterátor

Na závěr si pohrajte s [generátory][generátor] a [iterátory][iterátor]
a vytvořte si svůj vlastní [generátor][] a [iterátor][] pro fibonacciho 
posloupnost. (Můžete si také připomenout jak vypadá [generátorová notace][].)


[generátor]: http://diveintopython3.py.cz/generators.html#generators
[iterátor]: http://diveintopython3.py.cz/iterators.html
[generátorová notace]: http://diveintopython3.py.cz/comprehensions.html

