# problem part
import random

origin_state = [2, 8, 3, 1, 4, 5, 7, 6, 0]
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]


def reverse_num(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i] != 0 and arr[j] > arr[i]:
                res += 1
    return res


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
        temp = []
        for i in range(9):
            temp.append(i)
        while reverse_num(temp)%2 != 1:
            random.shuffle(temp)
        self.state = temp

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
        open_table.append(self)
        steps = 0

        while len(open_table) > 0:
            curr = open_table.pop(0)
            substates = curr.generate_substates(steps, False)
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
        open_table.append(self)
        steps = 0

        while len(open_table) > 0:
            curr = open_table.pop(0)
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
            open_table = sorted(open_table, key=lambda x: x.cost)
            steps += 1
        else:
            return None, None

    def solve(self, method="Astar"):
        if method == "BFS":
            return self.BFS()
        elif method == "Astar":
            return self.Astar()


# puz = puzzle(state=origin_state)
# path, step = puz.solve("Astar")
# path.append(puzzle(goal))

# GUI part
import tkinter as tk
import time

window = tk.Tk()
window.title("8-puzzle")
window.geometry('400x300')
window.resizable(width=False, height=False)
canvas = tk.Canvas(width=400, height=300)
puz = puzzle()

class block:
    def __init__(self, text, x, y, color):
        self.rect = canvas.create_rectangle(x, y, x + 50, y + 50, fill=color)
        self.text = canvas.create_text(x + 25, y + 25, text=text)


def paint_board(state):
    t = 0
    for i in range(3):
        for j in range(3):
            if state[t] == 0:
                block("", 50 + 50 * j, 20 + 50 * i, 'white')
            else:
                block(state[t], 50 + 50 * j, 20 + 50 * i, 'yellow')
            t += 1


def paint_result(paths):
    paint_button.config(state="disabled")
    for i in paths:
        paint_board(i.state)
        window.update()
        time.sleep(0.5)
    paint_button.config(state="normal")

def random_init():
    puz.random_init()
    paint_board(puz.state)

def solve(method = "Astar"):
    puz.solve(method)

paint_board([0,0,0,0,0,0,0,0,0])
radio = tk.StringVar()
text = tk.StringVar()
text.set("Steps: ")

paint_button = tk.Button(text="paint", width=5)#, command=lambda: paint_result(path)
paint_button.place(x=50, y=200)

run_button = tk.Button(text="run", width=5, command=lambda :solve(radio.get()))
run_button.place(x=100, y=200)

init_button = tk.Button(text="init", width=5, command=random_init)
init_button.place(x=150, y=200)


def display():
    text.set("Steps: " + radio.get())


step_text = tk.Label(window, textvariable = text).place(x=275, y=120)
method_text = tk.Label(window, textvariable = radio).place(x=275, y=140)

tk.Radiobutton(window, text="BFS", variable=radio, value='BFS', command=display).place(x=275, y=20)
tk.Radiobutton(window, text="Astar", variable=radio, value='Astar', command=display).place(x=275, y=40)
tk.Radiobutton(window, text="Other", variable=radio, value='Other', command=display).place(x=275, y=60)



canvas.pack()
window.mainloop()
