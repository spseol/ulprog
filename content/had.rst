Had nebo žížala, jednoduchá hra
########################################

:tags: středně pokročilý, OOP, TkInter, hra
:category: úloha


Úlokolem je vytvořit jednoduchou hru Had nebo Červ. Je jen na vás, co zvolíte 
a jak bude vypadat výsledek. Protože naše hra je maximálně jednoduchá postačí 
nám knihovna `TkInter <http://tkinter.programujte.com/>`_ 
a její `Canvas <http://tkinter.programujte.com/canvas.htm>`_.

Začít můžete s následujícím kódem. Nejprve třídu ``App``. Ta má za úkol
vytvořit okno a umístit do něj plátno (``Canvas``).  Každých 200 ms se spustí
funkce ``tickej`` a provede všechny funkce zaregistrované pomocí
``tick_register``. Při stisku klávesy Escape se aplikace ukončí.

.. code-block:: python
    :hl_lines: 19 22 27 30 
    :linenos: none
    :lineanchors: line
    :anchorlinenos: 

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

Dále vytvoříme třídu ``Snake``, kterou máte za úkol dotvořit, protože náš had
je tvořen jen jedním čtverečkem. Umí se pohybovat nahoru, dolů, doleva a
doprava ale tento pohyb je ještě hodně nedokonalý. Návodem, jak pohyb
zdokonalit vám může být funkce ``down``. Všimněte si také funkce ``tickej``,
která se volá každých 200 ms.

Každý čtvereček, který je vykreslen más svůj identifikátor ``self.id``. Pro
hada tořeného více čtverečky bude vhodné tento kód předělat tak aby to byl
seznam. 

**Relativní pohyb** 
  je realizován metodou  ``.move(id, posun_x, posun_y)``.

**Aktuální pozici**  
  získáme medodou ``.coords(id)``

**Přesun na absolutní pozici**
  zajístíme také pomocí funkce ``.coords(id, x1, y1, x2, y2)``. Souřednice jsou 
  dvě protože se jedná o levý horní a pravý dolní roh.

.. code-block:: python
    :hl_lines: 15 17 32 7 18 19
    :linenos: inline
    :lineanchors: line
    :anchorlinenos: 

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


No a teď si vyzkoušíme, jak nám to hezky chodí. Uděláme si dva hady. jeden se 
ovládá pomocí šipek, dryhý pomocí A, S, D, W.

.. code-block:: python

    if __name__ == '__main__':
        root = Tk()
        app = App(root, 80, 60, 20)
        snake = Snake(app)
        snake2 = Snake(app, color='red', down="s", up='w', left='a', right='d')
        root.mainloop()

Celý zdrojový kód si můžete stáhnout.


Varianta had
=============

Jak má celá hra vypadat záleží na vás. Jedna klasika je had. Ten se plazí 
a když něco sežere hezky nám naroste.


Varianta žížala
=================

Kdysi za éry dosu jsme hráli takový malý závod. Každý má svou žížalu a ta leze
z díry a je delší a delší. Ovládat ji musím tak, abych nenarazil ani do zdi,
ani do soupeře ani sám do sebe.
