Title: Kalendář
Date: 2015-04-30 09:39
Category: úloha
Tags: podmínky a cykly, mírně pokročilý
Author: Marek Nožka


Vypište na obrazovku kalendář ve tvaru:

    Po Út St Čt Pá So Ne
        1  2  3  4  5  6  
     7  8  9 10 11 12 13  
    14 15 16 17 18 19 20  
    21 22 23 24 25 26 27  
    28 29 30 31  
  
Tato úloha nespočívá v pouhém nalezení modulu (Calendar), který kalendář
umí vypsat! Je potřeba jej opravdu naprogramovat.

Aktuální datum, nebo měsíc zjistíte pomocí modulu `datetime`:
<http://docs.python.org/2.7/library/datetime.html>, ale není to až tak zapotřebí. 
Pro začátek stačí, když program bude načítat první den v týdnu, který připadá 
na první den měsíce. Například program, generující výše zmíněnou ukázku by přijal 
jako vstup číslo `2`, protože měsíc začíná úterkem.

    :::pycon
    >>> import datetime
    >>> today=datetime.date.today()
    >>> today.month
    10
    >>> today.day
    30
    >>> today.year
    2012
    >>> today.weekday()
    1
    >>> datetime.date(2012,10,31).weekday()
    2
    >>> datetime.date(2012,10,28).weekday()
    6
    >>> dayCount=[None,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

