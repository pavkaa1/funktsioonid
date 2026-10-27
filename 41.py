import tkinter as tk

def joonista_ring(canvas, x, y, raadius, varv):
    canvas.create_oval(
        x - raadius, y - raadius,
        x + raadius, y + raadius,
        fill=varv
    )

aken = tk.Tk()
aken.title("Värvilised ringid")

canvas = tk.Canvas(aken, width=500, height=400, bg="white")
canvas.pack()

varvid = ["red", "blue", "green", "yellow", "purple",
          "orange", "pink", "cyan", "brown", "magenta"]

for i in range(10):
    x = 50 + i * 40
    y = 100 + (i % 3) * 80
    raadius = 15 + i % 4 * 5
    joonista_ring(canvas, x, y, raadius, varvid[i])

aken.mainloop()