from grid import LifeGrid
from patterns import Pattern, get_pattern, get_all_patterns
import time

get_pattern("Blinker")

"""
blinker = Pattern("Blinker", {(2, 1), (2, 2), (2, 3)})
grid = LifeGrid(blinker)

print(grid.as_string((0, 0, 5, 5)))

grid.evolve()
print(grid.as_string((0, 0, 5, 5)))

grid.evolve()
print(grid.as_string((0, 0, 5, 5)))


grid.evolve()
print(grid.as_string((0, 0, 5, 5)))

i = 0

while i < 100:
    grid.evolve()
    print(grid.as_string((0, 0, 5, 5)))
    i = i + 1

    time.sleep(1)
"""
