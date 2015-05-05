Title: Začátečnické cvičení
Date: 2015-05-05 22:24
Category: úloha
Author: Marek Nožka
Tags: podmínky a cykly, začátečník


Zde je několik málo úloh na procvičení podmínek a cyklů. Vstup je brán vždy z
klávesnice. Můžete použít funkci `input()` nebo `raw_input()`. Pro tisk
použijte funkci `print`.


    :::python
    retezec = raw_input('zadej libovolný řetězec')
    cislo = input('zadej číslo')
    type(retezec)
    type(cislo)
    print retezec, cislo 


Také se bude jistě hodit metoda `str.split()`.

    :::python
    retezec = "1  2  abc d eee      ff"
    seznam = retezec.split()
    print seznam
    type(seznam)



 1. Je dána posloupnost znaků. Určete počet různých sudých **cifer**, které se
    zde nacházejí.

        zadej znaky > 23 15 ahoj 18 jedna 9 4441
        >>>>>>>>>>>>> v tomto řetězci je 5 sudých cifer  

 2. Je dána posloupnost celých čísel oddělených mezerou. 
    Pro záporná čísla vypište na obrazovku jejich druhou mocninu. 
    Pro kladná čísla vypište na obrazovku jejich odmocninu.

        zadej čísla > 9 -9 -12 3 2
        >>>>>>>>>>>>> 3 81 144 1.7320 1.4142

 3. Je dána posloupnost celých čísel. Přerovnejte čísla tak, aby na začátku
    posloupnosti byla všechna záporná čísla v původním pořadí a za nimi
    všechna nezáporná čísla opět se zachováním jejich původního pořadí. Upravenou
    posloupnost vypište.

        zadej čísla > -12 5 4 8 9 -1 
        >>>>>>>>>>>>> -12 -1 5 4 8 9

 4. Je dána posloupnost celých čísel. Přerovnejte čísla tak, aby na začátku
    posloupnosti byla všechna záporná čísla v původním pořadí a za nimi všechna
    nezáporná čísla v __opačném__ pořadí. Upravenou posloupnost vypište.

        zadej čísla > -12 5 4 8 9 -1 
        >>>>>>>>>>>>> -12 -1 9 8 4 5
