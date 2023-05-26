import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=2000, height=1500);

canvas.pack()

radius = 2

def handleDrag(event):
	x = event.x
	y = event.y
	canvas.create_oval(x - radius , y - radius , x + radius , y + radius, fill="red", outline="red")

def handleClick(event):
	x = event.x
	y = event.y
	canvas.create_oval(x - radius , y - radius , x + radius , y + radius, fill="red", outline="red")

def clearCanvas(event):
	canvas.delete("all")

canvas.bind("<B1-Motion>", handleDrag)
canvas.bind("<Button-1>", handleClick)

canvas.bind("<Key-c>", clearCanvas)

canvas.focus_set()

root.mainloop()
