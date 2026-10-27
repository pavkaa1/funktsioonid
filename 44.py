import tkinter as tk
import math
import random

def joonista_taht(canvas, x, y, suurus, varv):
    punktid = []

    for i in range(10):
        nurk = math.radians(i * 36 - 90)

        if i % 2 == 0:
            r = suurus
        else:
            r = suurus * 0.4

        px = x + r * math.cos(nurk)
        py = y + r * math.sin(nurk)

        punktid.extend([px, py])

    canvas.create_polygon(punktid, fill=varv, outline=varv)

aken = tk.Tk()
aken.title("Tähtede muster")

canvas = tk.Canvas(aken, width=600, height=400, bg="midnight blue")
canvas.pack()

varvid = ["yellow", "white", "gold", "light yellow"]

for i in range(25):
    x = random.randint(20, 580)
    y = random.randint(20, 380)
    suurus = random.randint(5, 15)
    varv = random.choice(varvid)

    joonista_taht(canvas, x, y, suurus, varv)

aken.mainloop()