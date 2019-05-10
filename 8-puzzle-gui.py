# problem part
import random

origin_state = [2,8,3,1,4,5,7,6,0]
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

class puzzle:
    def __init__(self, state=None, pre_move=None, parent=None):
        self.state = state
        self.directions = ["up", "down", "left", "right"]
        if pre_move:
            self.directions.remove(pre_move)
        self.pre_move = pre_move
        self.parent = parent
        self.cost = 0

    def random_init(self):
        for i in range(9):
            self.state.append(i)
        random.shuffle(self.state)

    def get_space(self):
        for i in range(9):
            if self.state[i] == 0:
                return i

    def print(self):
        c = 0
        for i in range(3):
            for j in range(3):
                print(self.state[c], end=" ")
                c += 1
            print("\n")
        print("  ↓\n")

    def cal_cost(self, step):
        eva = 0
        for i in range(9):
            eva += not (self.state[i] == goal[i])
        self.cost = eva + step

    def generate_substates(self, step, Astar):
        if not self.directions:
            return []
        substates = []
        space = self.get_space()

        # check the state if it can move. If so, move it
        if "up" in self.directions and space < 6:
            temp = self.state.copy()
            temp[space], temp[space + 3] = temp[space + 3], temp[space]
            new_puz = puzzle(temp, pre_move="up", parent=self)
            if Astar:
                new_puz.cal_cost(step)
            substates.append(new_puz)
        if "down" in self.directions and space > 2:
            temp = self.state.copy()
            temp[space], temp[space - 3] = temp[space - 3], temp[space]
            new_puz = puzzle(temp, pre_move="down", parent=self)
            if Astar:
                new_puz.cal_cost(step)
            substates.append(new_puz)
        if "left" in self.directions and space % 3 < 2:
            temp = self.state.copy()
            temp[space], temp[space + 1] = temp[space + 1], temp[space]
            new_puz = puzzle(temp, pre_move="left", parent=self)
            if Astar:
                new_puz.cal_cost(step)
            substates.append(new_puz)
        if "right" in self.directions and space % 3 > 0:
            temp = self.state.copy()
            temp[space], temp[space - 1] = temp[space - 1], temp[space]
            new_puz = puzzle(temp, pre_move="right", parent=self)
            if Astar:
                new_puz.cal_cost(step)
            substates.append(new_puz)

        return substates

    def BFS(self):
        open_table = []
        close_table = []

        open_table.append(self)
        steps = 0

        while len(open_table) > 0:
            curr = open_table.pop(0)
            close_table.append(curr)
            substates = curr.generate_substates(steps,False)
            path = []

            for i in substates:
                if i.state == goal:
                    while i.parent and i.parent != origin_state:
                        path.append(i.parent)
                        i = i.parent
                    path.reverse()
                    return path, steps + 1
            open_table.extend(substates)
            steps += 1
        else:
            return None, None

    def Astar(self):
        open_table = []
        close_table = []

        open_table.append(self)
        steps = 0

        while len(open_table) > 0:
            curr = open_table.pop(0)
            close_table.append(curr)
            substates = curr.generate_substates(steps, True)
            path = []

            for i in substates:
                if i.state == goal:
                    while i.parent and i.parent != origin_state:
                        path.append(i.parent)
                        i = i.parent
                    path.reverse()
                    return path, steps + 1
            open_table.extend(substates)
            open_table = sorted(open_table, key=lambda x:x.cost)
            steps += 1
        else:
            return None, None

    def solve(self,method="BFS"):
        if method=="BFS":
            return self.BFS()
        elif method=="Astar":
            return self.Astar()


puz = puzzle(state=origin_state)
path, step = puz.solve("Astar")
path.append(puzzle(goal))

# GUI part
import tkinter as tk
import time

window = tk.Tk()
window.title("8-puzzle")
window.geometry('500x300')
canvas = tk.Canvas()

class block:
    def __init__(self, text, x, y, color):
        self.rect=canvas.create_rectangle(x,y,x+50,y+50, fill=color)
        self.text=canvas.create_text(x+25,y+25,text=text)

def paint_board(state):
    t=0 
    for i in range(3):
        for j in range(3):
            if state[t]==0:
                block("",20+50*j,20+50*i,'white')
            else:
                block(state[t],20+50*j,20+50*i,'yellow')
            t+=1

def paint_result(paths):
    button.config(state="disabled")
    for i in paths:
        paint_board(i.state)
        window.update()
        time.sleep(0.5)
    button.config(state="normal")
        
paint_board(origin_state)

button = tk.Button(text="paint",command=lambda:paint_result(path))
button.place(x=300,y=20)

canvas.pack()
window.mainloop()