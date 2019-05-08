import random


class puzzle:
    def __init__(self, state=None, pre_move=None, parent=None):
        self.state = state
        self.directions = ["up", "down", "left", "right"]
        if pre_move:
            self.directions.remove(pre_move)
        self.pre_move = pre_move
        self.parent = parent

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

    def generate_substates(self):
        if not self.directions:
            return []
        substates = []
        space = self.get_space()

        # check the state if it can move. If so, move it
        if "up" in self.directions and space < 6:
            temp = self.state.copy()
            temp[space], temp[space + 3] = temp[space + 3], temp[space]
            new_puz = puzzle(temp, pre_move="up", parent=self)
            substates.append(new_puz)
        if "down" in self.directions and space > 2:
            temp = self.state.copy()
            temp[space], temp[space - 3] = temp[space - 3], temp[space]
            new_puz = puzzle(temp, pre_move="down", parent=self)
            substates.append(new_puz)
        if "left" in self.directions and space % 3 < 2:
            temp = self.state.copy()
            temp[space], temp[space + 1] = temp[space + 1], temp[space]
            new_puz = puzzle(temp, pre_move="left", parent=self)
            substates.append(new_puz)
        if "right" in self.directions and space % 3 > 0:
            temp = self.state.copy()
            temp[space], temp[space - 1] = temp[space - 1], temp[space]
            new_puz = puzzle(temp, pre_move="right", parent=self)
            substates.append(new_puz)

        return substates

    def solve(self):
        open_table = []
        close_table = []

        open_table.append(self)
        steps = 0

        while len(open_table) > 0:
            curr = open_table.pop(0)
            close_table.append(curr)
            substates = curr.generate_substates()
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


origin_state = [0, 2, 1, 3, 4, 5, 6, 7, 8]
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
puz = puzzle(state=origin_state)
path, step = puz.solve()
if path:
    for n in path:
        n.print()
    c = 0
    for i in range(3):
        for j in range(3):
            print(goal[c], end=" ")
            c += 1
        print("\n")
    print("total steps: %d" % step)
