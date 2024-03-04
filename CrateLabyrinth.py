import keyboard
import time
import os
import copy
import re

class GameState:
    def __init__(self, level):
        self.level(level)
        self.hero = self.find_hero()
        self.victory = False
        self.graphics()

    def level(self, level):
        filename = level
        labyrinth = []
        with open(filename) as level_played:
            all = level_played.read()
            pattern = r'\((.*?)\)'
            match = re.findall(pattern, all)
            destinations = []
            for elem in match:
                destination = (int(elem[0]), int(elem[2]))
                destinations.append(destination)
            self.destinations = destinations
            level_played = open(filename, "r")
            lines = level_played.readlines()
            for line in lines:
                row = []
                for char in line[0:-1]:
                    if char == "[":
                        break
                    else:
                        row.append(str(char))
                labyrinth.append(row)
            self.labyrinth = labyrinth[:-1]

    def graphics(self):
        os.system('cls')
        highlighted_destinations = copy.deepcopy(self.labyrinth)
        for destination in self.destinations:
            if highlighted_destinations[destination[0]][destination[1]] == " ":
                highlighted_destinations[destination[0]][destination[1]] = "X"
        for row in highlighted_destinations:
            print(row)

    def find_hero(self):
        row_index = 0
        for row in self.labyrinth:
            column_index = 0
            for column in row:
                if column == "H":
                    return row_index, column_index
                column_index += 1
            row_index += 1
        raise ValueError("There is no hero here")

    def step(self, direction):
        row_index, column_index = self.hero

        if direction == "w":
            step = self.labyrinth[row_index - 1][column_index]
            if step == " ":
                self.labyrinth[row_index - 1][column_index] = "H"
                self.labyrinth[row_index][column_index] = " "
                self.hero = row_index - 1, column_index
            if step == "C":
                if self.labyrinth[row_index - 2][column_index] == " ":
                    self.labyrinth[row_index - 2][column_index] = "C"
                    self.labyrinth[row_index - 1][column_index] = "H"
                    self.labyrinth[row_index][column_index] = " "
                    self.hero = row_index - 1, column_index

        if direction == "s":
            step = self.labyrinth[row_index + 1][column_index]
            if step == " ":
                self.labyrinth[row_index + 1][column_index] = "H"
                self.labyrinth[row_index][column_index] = " "
                self.hero = row_index + 1, column_index
            if step == "C":
                if self.labyrinth[row_index + 2][column_index] == " ":
                    self.labyrinth[row_index + 2][column_index] = "C"
                    self.labyrinth[row_index + 1][column_index] = "H"
                    self.labyrinth[row_index][column_index] = " "
                    self.hero = row_index + 1, column_index

        if direction == "a":
            step = self.labyrinth[row_index][column_index - 1]
            if step == " ":
                self.labyrinth[row_index][column_index - 1] = "H"
                self.labyrinth[row_index][column_index] = " "
                self.hero = row_index, column_index - 1
            if step == "C":
                if self.labyrinth[row_index][column_index - 2] == " ":
                    self.labyrinth[row_index][column_index - 2] = "C"
                    self.labyrinth[row_index][column_index - 1] = "H"
                    self.labyrinth[row_index][column_index] = " "
                    self.hero = row_index, column_index - 1

        if direction == "d":
            step = self.labyrinth[row_index][column_index + 1]
            if step == " ":
                self.labyrinth[row_index][column_index + 1] = "H"
                self.labyrinth[row_index][column_index] = " "
                self.hero = row_index, column_index + 1
            if step == "C":
                if self.labyrinth[row_index][column_index + 2] == " ":
                    self.labyrinth[row_index][column_index + 2] = "C"
                    self.labyrinth[row_index][column_index + 1] = "H"
                    self.labyrinth[row_index][column_index] = " "
                    self.hero = row_index, column_index + 1

        self.graphics()
        self.victory = self.check_victory()

    def check_victory(self):
        return all([self.labyrinth[destination[0]][destination[1]] == "C" for destination in self.destinations])


def get_user_input(): # no return, so it keeps running
    if keyboard.is_pressed("w"):
        time.sleep(0.3)
        return "w"
    if keyboard.is_pressed("s"):
        time.sleep(0.3)
        return "s"
    if keyboard.is_pressed("a"):
        time.sleep(0.3)
        return "a"
    if keyboard.is_pressed("d"):
        time.sleep(0.3)
        return "d"
    if keyboard.is_pressed("r"):
        time.sleep(0.3)
        return "reset"

labyrinth1 = GameState("Sokoban_Level_1.txt")

while not labyrinth1.victory:
    direction = get_user_input()
    if direction == "reset":
        labyrinth1 = GameState("Sokoban_Level_1.txt")
    elif direction:
        labyrinth1.step(direction)


labyrinth1.level("Sokoban_Level_1.txt")