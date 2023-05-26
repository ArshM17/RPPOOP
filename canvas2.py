import tkinter as tk

# Function to handle rectangle button click event
def draw_rectangle():
    canvas.bind("<Button-1>", start_rectangle)

# Function to handle triangle button click event
def draw_triangle():
    canvas.bind("<Button-1>", start_triangle)

def add_triangle_point(event):
    triangle_points.extend([event.x, event.y])
    if len(triangle_points) == 6:
        canvas.unbind("<Button-1>")
        canvas.create_polygon(triangle_points, outline="black")

def add_rectangle_point(event):
    rectangle_points.extend([event.x, event.y])
    if len(rectangle_points) == 8:
        canvas.unbind("<Button-1>")
        canvas.create_polygon(rectangle_points, outline="black")

def start_rectangle(event):
    global rectangle_points
    rectangle_points = [event.x, event.y]
    canvas.bind("<Button-1>", add_rectangle_point)

def start_triangle(event):
    global triangle_points
    triangle_points = [event.x, event.y]
    canvas.bind("<Button-1>", add_triangle_point)

# Function to handle canvas click event to add triangle points
# Create the main window
window = tk.Tk()
window.title("Shape Drawer")

# Create the canvas
canvas = tk.Canvas(window, width=800, height=800)
canvas.pack()

# Create the rectangle button
rectangle_button = tk.Button(window, text="Rectangle", command=draw_rectangle)
rectangle_button.pack(side="left")

# Create the triangle button
triangle_button = tk.Button(window, text="Triangle", command=draw_triangle)
triangle_button.pack(side="left")

# Start the tkinter event loop
window.mainloop()

