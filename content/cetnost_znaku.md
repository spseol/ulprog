Title: Četnost znaků
Date: 2015-05-05 22:34
Category: úloha
Tags: mírně pokročilý, slovník
Author: Marek Nožka



Vytvořte program, který ze standardního vstupu nebo ze souboru načte text a
vypíše četnosti jednotlivých znaků textu na obrazovku. Četnosti znaků zobrazte
nejen jako číselný údaj ale i graficky pomocí jednoduchého horizontálního
bargrafu. Až se vám bargraf povede udělat horizontálně udělejte ho vertikálně.

Malá pomoc:
==============

    :::python
    from sys import stdin, stdout, stderr

    cetnosti = {}

    while 1:
        line = stdin.readline()
        if not line:
            break
        line = line.decode('utf-8')
        line = line.strip()
        ...
        ...

    # tiskne seřazené četnosti
    for znak in sorted(cetnosti.keys()):
        print znak,'->',cetnosti[znak]

    # poměrně neefektvní zjištění maximální četnosti znaku
    hodnoty = cetnosti.values()  # všechny hodnoty ve slovníku
    hodnoty.sort()               # seřadím je
    hodnoty.reverse()            # nejčetnější je na začátku
    print "nejčetnější znak je zastoupen", hodnoty[0] , "krát"

    print 20*"*"


Příklad použití programu
==========================

Můžete si jednoduše ověřit, proč se v Morseově abecedě píše `E` jako `.`:

    $ w3m -dump 'http://en.wikipedia.org/wiki/Transistor' | cstocs utf-8 ascii | cetnost-znaku.py
    0     245 **
    1     222 **
    2     223 **
    3      97 
    4      88 
    5     124 *
    6      59 
    7      73 
    8      54 
    9     109 *
    A    2914 ***************************
    B     637 *****
    C    1628 ***************
    D    1307 ************
    E    4293 ****************************************
    F     804 *******
    G     716 ******
    H    1266 ***********
    I    2971 ***************************
    J     149 *
    K     168 *
    L    1518 **************
    M     995 *********
    N    2679 ************************
    O    2571 ***********************
    P     909 ********
    Q      49 
    R    2664 ************************
    S    2628 ************************
    T    3456 ********************************
    U     967 *********
    V     432 ****
    W     466 ****
    X      79 
    Y     448 ****
    Z      36 
