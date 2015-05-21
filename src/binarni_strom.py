#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  mujstrom.py
# Datum:   29.04.2015 22:41
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Autor:
# http://www.arungeek.com/binary-search-tree-in-python-with-ascii-art-visualization/
# Úloha:   pokus o implementaci binárního stromu
############################################################################
from __future__ import division, print_function, unicode_literals


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
    u20 = Uzel(20)
    u10 = Uzel(10)
    u15 = Uzel(15)
    u8 = Uzel(8)
    strom = Strom()
    print(strom.tisk())
    strom.koren = u15
    u15.vpravo = u20
    u15.vlevo = u8
    u8.vlevo = Uzel(6)
    u8.vpravo = Uzel(12)
    print()
    print(strom.tisk())
    print()
    print(7, 16)
    strom.vlozit(7)
    strom.vlozit(16)
    print()
    print(strom.tisk())
