#!/usr/bin/env python2
# -*- coding: utf8 -*-
# Soubor:  wormsnake.py
# Datum:   13.05.2015 08:48
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Pokouším se napast hru žížaloHAD.
####################################################

from Tkinter import (Tk, Canvas)
from random import randint


class App:
    ticklist = []    # seznam funkcí, které se budou spouštět při tiku
    tick_id = None   # identifikárot následujícího ticku

    def __init__(self, root, width=80, height=60, grid=10, tick=200):
        self.root = root      # objekt okna
        self.width = width    # šířka, jako počet sloupců
        self.height = height  # výška, jako počet řádků
        self.grid = grid      # kolik pixelů má jeden čtverec sítě
        self.tick = tick      # počet milisekund pro jeden úder hodin
        root.title("had.py")  # titulek okna
        self.canvas = Canvas(root, bg='white',
                             width=grid*width, height=grid*height)
        self.canvas.pack()
        root.bind("<Escape>", self.destroy)
        root.after(self.tick, self.tickej)

    def tickej(self):
        for f in self.ticklist:
            f()
        self.tick_id = self.root.after(self.tick, self.tickej)

    def tick_register(self, fnc):
        self.ticklist.append(fnc)

    def destroy(self, event=None):
        self.root.after_cancel(self.tick_id)
        root.destroy()


class Snake:
    def __init__(self, app, color="blue",
                 down="<Down>", up="<Up>", left="<Left>", right="<Right>"):
        self.id = app.canvas.create_rectangle(0, 0, app.grid, app.grid,
                                              outline=color,
                                              fill=color)
        app.canvas.move(self.id,
                        app.grid * randint(0, app.width-1),
                        app.grid * randint(0, app.height-1))
        app.root.bind(down, self.down)
        app.root.bind(up, self.up)
        app.root.bind(left, self.left)
        app.root.bind(right, self.right)

        app.tick_register(self.tickej)

    def down(self, event=None):
        app.canvas.move(self.id, 0, app.grid)
        x1, y1, x2, y2 = app.canvas.coords(self.id)
        if y2 > app.height * app.grid:
            app.canvas.coords(self.id, x1, 0, x2, app.grid)

    def up(self, event):
        app.canvas.move(self.id, 0, -app.grid)

    def left(self, event):
        app.canvas.move(self.id, -app.grid, 0)

    def right(self, event):
        app.canvas.move(self.id, app.grid, 0)

    def tickej(self, event=None):
        self.down()

if __name__ == '__main__':
    root = Tk()
    app = App(root, 70, 60, 12)
    snake = Snake(app)
    snake2 = Snake(app, color='red', down="s", up='w', left='a', right='d')
    root.mainloop()
