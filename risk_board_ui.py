from tkinter import *

polygon_coords = [[5, 50, 70, 85],
[65, 40, 135, 55],
[210, 0, 110, 115],
[75, 95, 70, 55],
[140, 95, 50, 70],
[190, 90, 65, 80],
[75, 150, 80, 80],
[125, 160, 100, 90],
[85, 215, 70, 90, ],
[140, 280, 100, 60],
[130, 315, 100, 100],
[155, 305, 140, 135],
[170, 385, 70, 140, ],
[310, 270, 120, 130],
[390, 290, 75, 50],
[425, 325, 90, 130],
[385, 365, 80, 80],
[395, 420, 90, 105],
[480, 440, 50, 75, ],
[310, 85, 50, 35],
[365, 55, 75, 90],
[415, 60, 120, 180],
[280, 125, 70, 80],
[355, 135, 75, 75],
[360, 190, 75, 80],
[300, 190, 65, 90, ],
[610, 360, 90, 75],
[690, 345, 70, 55],
[650, 415, 100, 100],
[705, 405, 85, 125, ],
[615, 270, 65, 85],
[535, 225, 90, 140],
[560, 165, 135, 125],
[610, 135, 100, 80],
[705, 135, 50, 100],
[600, 90, 90, 75],
[615, 25, 80, 80],
[660, 35, 115, 140],
[540, 10, 100, 175],
[485, 150, 90, 100],
[520, 35, 70, 150],
[420, 230, 125, 120]]

# Create a window
root = Tk()

current_player_text = Label(root, text = "current player")

current_player_text.pack()

B = Button(root, text="ON")

B.pack()

# Create a canvas
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()

polygons = []

poly_storage = []

for i in polygon_coords:
    # Define the vertices of the polygon
    vertices = [(i[0], i[1]), (i[0] + i[2], i[1]), (i[0] + i[2], i[1] + i[3]), (i[0], i[1] + i[3])]
    polygons.append(vertices)
    
for i, verts in enumerate(polygons):
    polygon = canvas.create_polygon(verts, outline='black', fill='white')
    canvas.tag_bind(polygon, '<Button-1>', lambda event, index=i: handle_click(event, index))
    canvas.create_text((verts[0][0] + verts[2][0])/2, (verts[0][1] + verts[2][1])/2, text=str(i), fill="black", font=('Helvetica 15 bold'))
    poly_storage.append(polygon)
    
# Define the function to be called when the polygon is clicked
def polygon_clicked(index):
    # Change the fill color of the polygon
    canvas.itemconfig(poly_storage[index], fill='red')

# Define a function to handle the click event
def handle_click(event, polygon):
    # Check if the click event occurred on the polygon
    polygon_clicked(polygon)
    #if polygon in canvas.find_withtag(CURRENT):
    #    callback()

# Run the window
root.mainloop()

class ui:
    def __init__(self, board):
        self.game_board = board
        