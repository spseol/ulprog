Počítání pro ZŠ
####################################

:tags: mírně pokročilý, vstup/výstup, podmínky a cykly
:category: úloha

Vyvořte aplikaci, pro kontrolu početních dovedností žáků 3. třídy ZŠ. Aplikace
vygeneruje 12 příkladů, bude kontrolovat výsedky a na koci vždy vypíše počet
dobře a špatně zvládnutých úloh a procentní úspěšnost.

První krok -- odčítání
===========================

Generujte příklady pro odčítání do 100, tak abyste vyloučili záporné výsledky:

Např:

 * 76 - 65
 * 57 - 12
 * 38 - 9


Druhý krok -- dělení
===========================

Generujte příklady pro dělení beze zbitku z malé násobilky.

Např:

 * 56 : 7
 * 18 : 3
 * 81 : 9


Třetí krok -- plus, mínus krát děleno
=========================================

Generujte náhodně příklady na sčítání, odčítání, násobení a dělení.


Čtvrtý krok  -- výběr a priorita
==================================

Program si na začátku od uživatele vyžádá seznam operací, ze kterýh má zkoušet. 
Například ::
    
    zadej matematické operace (+-*:) >  +-:::

... program bude generovat úlohy na sčítání, odčítání a dělení. Přičemž 
generování úloh na dělení bude pravděpodobnější.

