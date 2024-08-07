#!/usr/bin/python3
"""
to get island Perimeter
"""

def island_perimeter(grid):
    """
    returns islands perimeter
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area
