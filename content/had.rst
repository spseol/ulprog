Had nebo Červ, jednoduchá hra
####################################

:tags: středně pokročilý, OOP, TkInter, hra
:category: úloha


Úlokolem je vytvořit jednoduchou hru Had nebo Červ. Je jen na vás, co zvolíte 
a jak bude vypadat výsledek. Protože naše hra je maximálně jednoduchá postačí 
nám knihovna `TkInter <http://tkinter.programujte.com/>`_ 
a její `Canvas <http://tkinter.programujte.com/canvas.htm>`_.

Začít můžete s následujícím kódem.

.. code-block:: python
    :hl_lines: 10 20 
    :linenos: table
    :lineanchors: line
    :anchorlinenos: 

    from Tkinter import (Tk, Canvas)
    from random import randint


    class App:
        def __init__(self, root, width=80, height=60, grid=10, tick=200):
            self.root = root
            root.title("had.py")
            root.option_add('*Font', 'Terminus 14')
            root.bind("<Escape>", exit)
            self.width = width    # šířka, jako počet sloupců
            self.height = height  # výška, jako počet řádků
            self.grid = grid      # kolik pixelů má jeden čtverec sítě
            self.tick = tick      # počet milisekund pro jeden úder hodin
            self.ticklist = []    # seznam funkcí, které se budou spouštět při tiku
            self.canvas = Canvas(root, bg='white',
                                width=grid*width, height=grid*height)
            self.canvas.pack()
            root.bind("<Escape>", self.destroy)
            root.after(self.tick, self.tickej)

        def tickej(self):
            for f in self.ticklist:
                f()
            root.after(self.tick, self.tickej)

        def tick_register(self, fnc):
            self.ticklist.append(fnc)

        def destroy(self, event=None):
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

            app.tick_register(self.down)

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

    if __name__ == '__main__':
        root = Tk()
        app = App(root, 80, 60, 8)
        snake = Snake(app)
        snake2 = Snake(app, color='red', down="s", up='w', left='a', right='d')
        root.mainloop()

aa
