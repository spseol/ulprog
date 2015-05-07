Title: Exponenciální funkce
Date: 2015-05-07 23:12
Category: úloha
Tags: mírně pokročilý, podmínky a cykly, funkce
Author: Marek Nožka

Vytvořte funkci `myexp`, která bude realizovat výpočet 
[exponenciální funkce](http://cs.wikipedia.org/wiki/Exponenciální_funkce).


    :::python
    def myexp(x):
        ...
        return ...

    print(myexp(1))
    print(math.exp(1))

Pro výpočet použijte
[Taylorovu řadu](https://cs.wikipedia.org/wiki/Taylorova_%C5%99ada)

$$e^x=1+\frac{x}{1!} + \frac{x^2}{2!}+...+\frac{x^n}{n!}$$

tedy

$$
e^x=1+\frac{x}{1} + \frac{x\cdot x}{1\cdot2}+
   \frac{x\cdot x \cdot x}{1 \cdot 2 \cdot 3} + 
   \frac{x\cdot x \cdot x \cdot x}{1 \cdot 2 \cdot 3 \cdot 4} + ...
$$

Řada je nekonečná ale konvergentní, takže velikost každého dalšího členu se
zmenšuje. Výpočet tedy zastavíme až jeho velikost neovlivní námi požadovanou
přesnost výsledku. Tedy například až bude menší než $10^{-5}$.

**Malá rada**:
: Všimněte si, že každý další člen posloupnosti je tvoře předchozím členem krát
  $\frac{x}{n}$.
