import tkinter as tk
from playsound import playsound
import math
import time
def main():
    root = tk.Tk()
    root.title("---The Maze---")
    level = 0
    levels = []
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()
    wall_ids = []
    finish_id =[]
    start_id =[]
    started = False
    # creates player circle
    player = None
    player_radius = 2
    def create_wall(x1, y1, x2, y2, **kwargs):
        wall = canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
        wall_ids.append(wall)
        return wall
    def level_1():
        nonlocal level, player
        wall_ids.clear()
        finish_id.clear()
        start_id.clear()
        canvas.delete('all')
        nonlocal started
        started = False
        canvas.create_rectangle(0, 0, 600, 400, fill="darkslategrey")
        for i in range (0, 400, 30):
            create_wall(0, 0+i, 60, 30+i, fill='black', outline='red', width = 2)
        for i in range(0, 600, 60):
            create_wall(90+i, 0, 170+i, 40, fill='black', outline='red', width = 2)
        canvas.unbind("<Button-1>")


        create_wall(500, 40, 600, 80, fill='black', outline='red', width = 1.6)          #all
        create_wall(500, 80, 550, 120, fill='black', outline='red', width = 1.6)         #this
        create_wall(550, 80, 600, 100, fill='black', outline='red', width = 1.6)         #functions
        create_wall(550, 100, 575, 120, fill='black', outline='red', width = 1.6)        #make
        create_wall(575, 100, 600, 110, fill='black', outline='red', width = 1.6)        #the upper-left corner
        create_wall(575, 110, 587.5, 120, fill='black', outline='red', width = 1.6)      #spiral
        create_wall(587.5, 110, 600, 120, fill='black', outline='red', width = 1.6)      #effect
        create_wall(60, 75, 90, 350, fill='black', outline='red', width = 2)      #left vertical long
        create_wall(60, 350, 350, 400, fill='black', outline='red', width = 2)    #bottom horizontal big
        create_wall(120, 250, 200, 310,  fill='black', outline='red', width = 2)  #loop core
        create_wall(235, 150, 285, 250, fill='black', outline='red', width = 2)   #curver
        create_wall(90, 150, 235, 220, fill='black', outline='red', width = 2)    #above loop core
        create_wall(200, 280, 315, 310, fill='black', outline='red', width = 2)   #under curver
        create_wall(285, 150, 450, 190, fill='black', outline='red', width = 2)   #next to curver
        create_wall(450, 150, 540, 350, fill='black', outline='red', width = 2)   #big right side loop core
        create_wall(390, 385, 600, 400, fill='black', outline='red', width = 2)   #thin bottom right
        create_wall(580, 120, 600, 385, fill='black', outline='red', width = 2)   #right edge
        create_wall(315, 220, 420, 310, fill='black', outline='red', width = 2)   #medium middle loop core
        create_wall(390, 310, 420, 385, fill='black', outline='red', width = 2)   #connection between med loop core and thin bott rt
        finish = canvas.create_oval(60, -15, 90, 15, fill= 'green')
        finish_id.append(finish)
        start = canvas.create_rectangle(350, 364, 390, 382, fill='blue')
        start_id.append(start)
        create_wall(0, 0, 600, 1, fill='')
        create_wall(600, 0, 600, 400, fill='')
        create_wall(0, 400, 600, 399, fill='')
        create_wall(0, 0, 1, 400, fill='')

        create_wall(135, 40, 500, 120, fill='black', outline='red', width = 5)    #upper colossal
        canvas.create_text(317.5, 80, text = f'level_{level + 1}' ,  fill='white', font = ('Terminal', 14))    #makes level name
        player = canvas.create_oval(0, 0, player_radius * 2, player_radius * 2, fill="blue")

        canvas.coords(player, 370 - player_radius, 400 - player_radius*2, 370 + player_radius*2, 400 + player_radius, )
        #levels.append(level_1)

    def level_2():
        nonlocal level, player
        wall_ids.clear()
        finish_id.clear()
        start_id.clear()
        canvas.delete('all')
        nonlocal started
        started = False
        canvas.unbind("<Button-1>")
        canvas.create_rectangle(0, 0, 600, 400, fill="darkslategrey")

        # Create zigzag walls (leave alternating gaps)
        gap_height = 140  # tighter gaps
        wall_width = 27.5
        create_wall(0, 0, 600, 1, fill = '')
        create_wall(600, 0, 600, 400, fill = '')
        create_wall(0, 400, 600, 399, fill = '')
        create_wall(0, 0, 1, 400, fill = '')

        for i in range(1, 10):
            x = i * 60
            if i % 2 == 0:
                # leave a gap at the bottom
                create_wall(x, 0, x + wall_width, 400 - gap_height, fill='black', outline='red', width=2)
            else:
                # leave a gap at the top
                create_wall(x, gap_height, x + wall_width, 400, fill='black', outline='red', width=2)

        # Start and Finish
        start = canvas.create_rectangle(5, 370, 35, 390, fill='blue')
        start_id.append(start)
        finish = canvas.create_oval(570, 10, 590, 30, fill='green')
        finish_id.append(finish)

        canvas.create_text(300, 20, text=f'level_{level + 1}', fill='white', font=('Terminal', 14))

        # Player setup
        player = canvas.create_oval(0, 0, player_radius * 2, player_radius * 2, fill="blue")
        canvas.coords(player, 20 - player_radius, 380 - player_radius, 20 + player_radius, 380 + player_radius)



    def level_3():
        nonlocal level, player
        wall_ids.clear()
        finish_id.clear()
        start_id.clear()
        canvas.delete('all')
        nonlocal started
        started = False
        canvas.unbind("<Button-1>")
        canvas.create_rectangle(0, 0, 600, 400, fill="darkslategrey")

        # Create zigzag walls (leave alternating gaps)
        gap_height = 40  # tighter gaps
        wall_width = 27.5
        create_wall(0, 0, 600, 1, fill = '')
        create_wall(600, 0, 600, 400, fill = '')
        create_wall(0, 400, 600, 399, fill = '')
        create_wall(0, 0, 1, 400, fill = '')

        for i in range(1, 10):
            x = i * 60
            if i % 2 == 0:
                # leave a gap at the bottom
                create_wall(x, 0, x + wall_width, 400 - gap_height, fill='black', outline='red', width=2)
            else:
                # leave a gap at the top
                create_wall(x, gap_height, x + wall_width, 400, fill='black', outline='red', width=2)

        # Start and Finish
        start = canvas.create_rectangle(5, 370, 35, 390, fill='blue')
        start_id.append(start)
        finish = canvas.create_oval(570, 10, 590, 30, fill='green')
        finish_id.append(finish)

        canvas.create_text(300, 20, text=f'level_{level + 1}', fill='white', font=('Terminal', 14))

        # Player setup
        player = canvas.create_oval(0, 0, player_radius * 2, player_radius * 2, fill="blue")
        canvas.coords(player, 20 - player_radius, 380 - player_radius, 20 + player_radius, 380 + player_radius)

    levels.append(level_1)
    levels.append(level_2)
    levels.append(level_3)
    def defeat_screen():
        playsound('Sound_effects/lose.mp3')
        canvas.delete('all')
        canvas.create_rectangle(0, 0, 600, 400, fill='white', outline='')
        canvas.create_text(300, 200, text='You Lose!', fill='red', font=('Terminal', 40))
        canvas.create_text(300, 250, text='Click anywhere to restart', fill='red', font=('Terminal', 10))
        canvas.bind("<Button-1>", restart)  # rebind click to restart
    def victory_screen():
        playsound('Sound_effects/win.mp3')
        canvas.delete('all')
        canvas.create_rectangle(0, 0, 600, 400, fill='white', outline='')
        canvas.create_text(300, 200, text='You Win!', fill='Green', font=('Terminal', 40))
        canvas.create_text(300, 250, text='Click anywhere to go to the next level', fill='red', font=('Terminal', 10))
        canvas.bind("<Button-1>", on_click)

    def restart(event):
        nonlocal level, levels
        canvas.unbind('<Button-1>')

        levels[level]()
        canvas.bind('<Button-1>', on_click)
        canvas.bind("<Motion>", follow_cursor)


    def follow_cursor(event):
        nonlocal started
        x, y = event.x, event.y
        print(f"Cursor at ({x}, {y})")
        if not started:
            overlapping = canvas.find_overlapping(x, y, x+1, y+1)
            for item in overlapping:
                if item in start_id:
                    started = True
                    print("Start zone touched!")
                    break
            if not started:
                return  # Don't move until player overlaps start zone

        # Allow movement after the game has started

        canvas.coords(player, x - player_radius, y - player_radius, x + player_radius, y + player_radius)
        coords = canvas.coords(player)
        overlapping = canvas.find_overlapping(*coords)

        for item in overlapping:
            if item in wall_ids:
                defeat_screen()
            if item in finish_id:
                victory_screen()

    canvas.bind("<Motion>", follow_cursor)

    # Function to update player position to follow cursor
    def on_click(event):
        nonlocal level
        level += 1
        if level < len(levels):
            levels[level]()
            canvas.bind("<Motion>", follow_cursor)
        else:
            canvas.delete("all")
            canvas.create_text(300, 200, text="You completed all levels!", font=("Terminal", 24), fill="green")
            return
        canvas.bind("<Motion>", follow_cursor)

    canvas.bind("<Button-1>", on_click)
    levels[level]()
    root.mainloop()
if __name__ == '__main__':
    main()
