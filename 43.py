import tkinter as tk

def joonista_silmad(canvas, x, y, suurus):
    canvas.create_oval(x - suurus * 0.2, y - suurus * 0.1,
                       x, y + suurus * 0.1, fill="black")
    canvas.create_oval(x + suurus * 0.2, y - suurus * 0.1,
                       x + suurus * 0.4, y + suurus * 0.1, fill="black")

def joonista_nina(canvas, x, y, suurus):
    canvas.create_polygon(
        x, y,
        x + suurus * 0.5, y + suurus * 0.1,
        x, y + suurus * 0.2,
        fill="orange"
    )

def joonista_nööbid(canvas, x, y, suurus):
    for i in range(3):
        canvas.create_oval(
            x - suurus * 0.05, y + i * suurus * 0.15,
            x + suurus * 0.05, y + i * suurus * 0.15 + suurus * 0.1,
            fill="black"
        )

def joonista_lumememm(canvas, x, y, suurus):
    # Kolm lumepalli
    canvas.create_oval(x - suurus, y, x + suurus, y + 2 * suurus,
                       fill="white", outline="black")
    canvas.create_oval(x - suurus * 0.75, y - suurus, 
                       x + suurus * 0.75, y + suurus * 0.5,
                       fill="white", outline="black")
    canvas.create_oval(x - suurus * 0.5, y - suurus * 2,
                       x + suurus * 0.5, y - suurus,
                       fill="white", outline="black")

    # Nägu ja nööbid
    joonista_silmad(canvas, x - suurus * 0.2, y - suurus * 1.5, suurus)
    joonista_nina(canvas, x, y - suurus * 1.3, suurus)
    joonista_nööbid(canvas, x, y + suurus * 0.3, suurus)

aken = tk.Tk()
aken.title("Lumememmed")

canvas = tk.Canvas(aken, width=600, height=450, bg="lightblue")
canvas.pack()

joonista_lumememm(canvas, 180, 250, 50)
joonista_lumememm(canvas, 420, 300, 30)

aken.mainloop()