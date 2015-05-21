Title: Binární strom
Date: 2015-05-21 10:12
Category: úloha
Tags: středně pokročilý, OOP, rekurze, struktury a algoritmy
Author: Marek Nožka



        _15_  
       /    \ 
      8_    20
    /  \   /\
    6   12 16 
    /\  /\ /\ 
     7        
    /\       


Vytvořte sadu funkcí (metod) pro práci s binárním stromem. Tedy: přidávání
prvku, mazání prvku, hledání prvku, případně vyvažování stromu.

* <http://cs.wikipedia.org/wiki/Binární_vyhledávací_strom>
* <http://cs.wikipedia.org/wiki/Řazení_haldou>
* [C++ Binární vyhledávací stromy](ttp://www.linuxsoft.cz/article.php?id_article=1772)
* [Recepty z programátorské kuchařky -- Vyhledávací stromy](https://ksp.mff.cuni.cz/tasks/18/cook4.html)



Jako základ pro vaši práci můžete použít [tento zdrojový
kód]({filename}./src/binarni_strom.py) 
(Tento [zdoj](http://www.arungeek.com/binary-search-tree-in-python-with-ascii-art-visualization/)
jsem použil protože má hezký ASCII-art tisk).

    :::python
    class Uzel(object):
        def __init__(self, klic, rodic=None):
            self.klic = klic
            self.vlevo = None
            self.vpravo = None
            self.rodic = rodic


    class Strom(object):
        def __init__(self):
            self.koren = None

        def vlozit(self, klic):
            if not self.koren:  # pokud je strom prázdný
                self.koren = Uzel(klic)
            else:
                hledacek = self.koren
                while True:
                    if klic < hledacek.klic:
                        if hledacek.vlevo:  # vlevo něco je
                            hledacek = hledacek.vlevo
                        else:  # vlevo nic není
                            hledacek.vlevo = Uzel(klic)
                            hledacek.rodic = hledacek
                            break
                    elif klic > hledacek.klic:
                        if hledacek.vpravo:  # vpravo něco je
                            hledacek = hledacek.vpravo
                        else:  # vpravo nic není
                            hledacek.vpravo = Uzel(klic)
                            hledacek.rodic = hledacek
                            break
                    else:  # narazil jsem na číslo, které ve stromu už je
                        break

        def tisk(self):
            if self.koren is None:
                return '<empty tree>'

            def traverse(node):
                if node is None:
                    return [], 0, 0  # lines | position | width
                label = str(node.klic)
                left_lines, left_pos, left_width = traverse(node.vlevo)
                right_lines, right_pos, right_width = traverse(node.vpravo)
                middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
                pos = left_pos + middle // 2
                width = left_pos + middle + right_width - right_pos
                while len(left_lines) < len(right_lines):
                    left_lines.append(' ' * left_width)
                while len(right_lines) < len(left_lines):
                    right_lines.append(' ' * right_width)
                if (middle - len(label)) % 2 == 1 and node is not None:
                    if node is node.vlevo:
                        if len(label) < middle:
                            label += b'_'
                label = label.center(middle, b'_')
                if label[0] == '_':
                    label = ' ' + label[1:]
                if label[-1] == '_':
                    label = label[:-1] + ' '
                lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                        ' ' * left_pos + '/' + ' ' * (middle - 2) +
                        '\\' + ' ' * (right_width - right_pos)] + \
                        [left_line + ' ' * (width - left_width - right_width) +
                        right_line
                        for left_line, right_line in zip(left_lines, right_lines)]
                return lines, pos, width
            return '\n'.join(traverse(self.koren)[0])


    if __name__ == '__main__':
        strom = Strom()
        strom.vlozit(7)
        strom.vlozit(16)
        strom.vlozit(12)
        strom.vlozit(9)
        strom.vlozit(1)
        print(strom.tisk())
