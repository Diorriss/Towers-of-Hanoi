""" Towers of Hanoi

Tags: Simulation, Recursive algorithm"""

# The towers where all the discs will move around on
Towers = ['a', 'b', 'c']  # The towers

"Prints all the steps to solve the towers of hanoi"

for disc1 in enumerate(Towers):  # Disc1 size 3
    for disc2 in enumerate(Towers):  # Disc2 size 2
        for disc3 in enumerate(Towers):  # Disc3 size 1
            print(str(disc1), str(disc2), str(disc3))
