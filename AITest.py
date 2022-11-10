#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    princess_col = 0
    man_col = 0
    princess_row = 0
    man_row = 0
    for i in range(len(grid)):
        princess_col = grid[i].find('p')
        if princess_col != -1:
            princess_row = i
            break
    for j in range(len(grid)):
        man_col = grid[j].find('m')
        if man_col != -1:
            man_row = j
            break
    rowdiff = princess_row - man_row
    if rowdiff > 0:
        # man needs to move down
        for x in range(rowdiff, 0, -1):
            print("DOWN")
    if rowdiff < 0:
        # man needs to move up
        for y in range(abs(rowdiff), 0, -1):
            print("UP")
    coldiff = princess_col - man_col
    if coldiff > 0:
        # man needs to move right
        for d in range(coldiff, 0, -1):
            print("RIGHT")
    if coldiff < 0:
        # man needs to move left
        for e in range(abs(coldiff), 0, -1):
            print("LEFT")
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)