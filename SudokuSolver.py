'''
Created on 10 Jan 2020

@author: Vincent
'''
# SUDOKU SOLVER

super_easy = [
        [0, 4, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 3, 0, 7, 5, 0, 6, 0],
        [0, 0, 0, 2, 0, 0, 5, 4, 3],
        [0, 7, 2, 0, 0, 0, 0, 3, 9],
        [0, 0, 0, 9, 4, 2, 0, 0, 0],
        [5, 9, 0, 0, 0, 0, 6, 2, 0],
        [1, 2, 7, 0, 0, 3, 0, 0, 0],
        [0, 5, 0, 1, 9, 0, 2, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 7, 0],
       ]
empty_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
       ]

def colPacker(inputGrid):
    # Reshuffles 9x9 sudoku grid so that each column becomes a row, and each row a column
    # for example the 9 [X][0]th items in the input 2D array become a array of len 9 as 0th element of output array
    colsGrid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
           ]
    for i in range(9):
        for x in range(9):
            colsGrid[i][x] = inputGrid[x][i]
    return colsGrid

def boxPacker(inputGrid):
    #converts each 3x3 sudoku box in the input grid into a single array of len 9
    boxsGrid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
           ]

    for i in range(9):
        for x in range(9):
            if i in [0,3,6]:
                if x<3:
                    boxsGrid[i][x] = inputGrid[i][x]
                elif x<6:
                    boxsGrid[i][x] = inputGrid[i+1][x-3]
                else:
                    boxsGrid[i][x] = inputGrid[i+2][x-6]
            if i in [1,4,7]:
                if x<3:
                    boxsGrid[i][x] = inputGrid[i-1][x+3]
                elif x<6:
                    boxsGrid[i][x] = inputGrid[i][x]
                else:
                    boxsGrid[i][x] = inputGrid[i+1][x-3]
            if i in [2,5,8]:
                if x<3:
                    boxsGrid[i][x] = inputGrid[i-2][x+6]
                elif x<6:
                    boxsGrid[i][x] = inputGrid[i-1][x+3]
                else:
                    boxsGrid[i][x] = inputGrid[i][x]
    return boxsGrid

def boxCoords(i, x):
    # given input coordinates of a cell, returns what the coordinates of that cell become after the grid
    # is put through boxCoords.
    new_i = 0
    new_x = 0
    if i in [0,3,6]:
        if x<3:
            new_i = i
            new_x = x
        elif x<6:
            new_i = i+1
            new_x = x-3
        else:
            new_i = i+2
            new_x = x-6
    if i in [1,4,7]:
        if x<3:
            new_i = i-1
            new_x = x+3
        elif x<6:
            new_i = i
            new_x = x
        else:
            new_i = i+1
            new_x = x-3
    if i in [2,5,8]:
        if x<3:
            new_i = i-2
            new_x = x+6
        elif x<6:
            new_i = i-1
            new_x = x+3
        else:
            new_i = i
            new_x = x
    return [new_i, new_x]

def findCandidates(inputGrid):
    boxsGrid = boxPacker(inputGrid)
    colsGrid = colPacker(inputGrid)
    candidates= [
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], []],
           ]
    for i in range(9):
        for x in range(9):
            if inputGrid[i][x]==0:
                for num in range(1,10):
                    if i<3 and x<3:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[0]:
                            candidates[i][x].append(num)
                    elif i<3 and x>=3 and x<6:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[1]:
                            candidates[i][x].append(num)
                    elif i<3 and i<6 and x>=6:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[2]:
                            candidates[i][x].append(num)

                    elif i>=3 and i<6 and x<3:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[3]:
                            candidates[i][x].append(num)
                    elif i>=3 and i<6 and x>=3 and x<6:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[4]:
                            candidates[i][x].append(num)
                    elif i>=3 and i<6 and x>=6:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[5]:
                            candidates[i][x].append(num)

                    elif i>5 and x<3:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[6]:
                            candidates[i][x].append(num)
                    elif i>5 and x>=3 and x<6:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[7]:
                            candidates[i][x].append(num)
                    else:
                        if num not in colsGrid[x] and num not in inputGrid[i] and num not in boxsGrid[8]:
                            candidates[i][x].append(num)
    return candidates

def occurs_once(num, thelist):
    return thelist.count(num) == 1

def occurs_twice(num, thelist):
    return thelist.count(num) == 2

def pair_trimmer(coord1, coord2, num, candidates):
    indexes = [0,1,2,3,4,5,6,7,8]

    if(coord1 == coord2):
        return candidates

    if(coord1[1] == coord2[1]):
        candidates = colPacker(candidates)
        row_num = coord1[1]

        indexes.remove(coord1[0])
        indexes.remove(coord2[0])

    elif(coord1[0] == coord2[0]):
        #then rows
        row_num = coord1[0]

        indexes.remove(coord1[1])
        indexes.remove(coord2[1])

    else:
        return candidates


    for i in indexes:
        for item in candidates[row_num][i]:
            if(item == num):
                candidates[row_num][i].remove(num)

    if(coord1[1] == coord2[1]):
        candidates = colPacker(candidates)

    return candidates

def pointing_pairs_trimmer(candidates):
    candidatesBoxes = boxPacker(candidates)

    for i in range(9):
        all_nums_in_box = []
        for x in candidatesBoxes[i]:
            all_nums_in_box += x

        doubles_list = []
        for y in range(1,10):
            if(occurs_twice(y, all_nums_in_box)):
                doubles_list.append(y)

        top_row = candidatesBoxes[i][0] + candidatesBoxes[i][1] + candidatesBoxes[i][2]
        mid_row = candidatesBoxes[i][3] + candidatesBoxes[i][4] + candidatesBoxes[i][5]
        bot_row = candidatesBoxes[i][6] + candidatesBoxes[i][7] + candidatesBoxes[i][8]
        left_col = candidatesBoxes[i][0] + candidatesBoxes[i][3] + candidatesBoxes[i][6]
        mid_col = candidatesBoxes[i][1] + candidatesBoxes[i][4] + candidatesBoxes[i][7]
        right_col = candidatesBoxes[i][2] + candidatesBoxes[i][5] + candidatesBoxes[i][8]

        for double in doubles_list:
            if occurs_twice(double, top_row):
                if double in candidatesBoxes[i][0] and double in candidatesBoxes[i][1]:
                    candidates = pair_trimmer(boxCoords(i,0), boxCoords(i,1), double, candidates)
                elif double in candidatesBoxes[i][0] and double in candidatesBoxes[i][2]:
                    candidates = pair_trimmer(boxCoords(i,0), boxCoords(i,2), double, candidates)
                else:
                    candidates = pair_trimmer(boxCoords(i,1), boxCoords(i,2), double, candidates)

            elif occurs_twice(double, mid_row):
                if double in candidatesBoxes[i][3] and double in candidatesBoxes[i][4]:
                    candidates = pair_trimmer(boxCoords(i,3), boxCoords(i,4), double, candidates)
                elif double in candidatesBoxes[i][3] and double in candidatesBoxes[i][5]:
                    candidates = pair_trimmer(boxCoords(i,3), boxCoords(i,5), double, candidates)
                else:
                    candidates = pair_trimmer(boxCoords(i,4), boxCoords(i,5), double, candidates)

            elif occurs_twice(double, bot_row):
                if double in candidatesBoxes[i][6] and double in candidatesBoxes[i][7]:
                    candidates = pair_trimmer(boxCoords(i,6), boxCoords(i,7), double, candidates)
                elif double in candidatesBoxes[i][6] and double in candidatesBoxes[i][8]:
                    candidates = pair_trimmer(boxCoords(i,6), boxCoords(i,8), double, candidates)
                else:
                    candidates = pair_trimmer(boxCoords(i,7), boxCoords(i,8), double, candidates)

            elif occurs_twice(double, left_col):
                if double in candidatesBoxes[i][0] and double in candidatesBoxes[i][3]:
                    candidates = pair_trimmer(boxCoords(i,0), boxCoords(i,3), double, candidates)
                elif double in candidatesBoxes[i][0] and double in candidatesBoxes[i][6]:
                    candidates = pair_trimmer(boxCoords(i,0), boxCoords(i,6), double, candidates)
                else:
                    candidates = pair_trimmer(boxCoords(i,3), boxCoords(i,6), double, candidates)

            elif occurs_twice(double, mid_col):
                if double in candidatesBoxes[i][1] and double in candidatesBoxes[i][4]:
                    candidates = pair_trimmer(boxCoords(i,1), boxCoords(i,4), double, candidates)
                elif double in candidatesBoxes[i][1] and double in candidatesBoxes[i][7]:
                    candidates = pair_trimmer(boxCoords(i,1), boxCoords(i,7), double, candidates)
                else:
                    candidates = pair_trimmer(boxCoords(i,4), boxCoords(i,7), double, candidates)

            elif occurs_twice(double, right_col):
                if double in candidatesBoxes[i][2] and double in candidatesBoxes[i][5]:
                    candidates = pair_trimmer(boxCoords(i,2), boxCoords(i,5), double, candidates)
                elif double in candidatesBoxes[i][2] and double in candidatesBoxes[i][8]:
                    candidates = pair_trimmer(boxCoords(i,2), boxCoords(i,8), double, candidates)
                else:
                    candidates = pair_trimmer(boxCoords(i,5), boxCoords(i,8), double, candidates)

    return candidates

def scanning_solve(candidates):
    ######TAKES A CANDIDATES GRID, RETURNS A CANDIDATES GRID WITH SOME INTS#######
    #replaces a list of potential numbers for a 1x1 square with the correct integer in a sudoku grid, if that 1x1 square
    #is the only one in it's 3x3 parent which has that number as a candidate - ie it is the only allowed place for that number
    #to go. returns a candidates grid which may contain some ints if progress was made.

    #find the candidates for the grid and reshuffle the arrays into 3x3 boxes
    candidatesBoxes = boxPacker(candidates)
    #create a second variable so we don't have to mutate the input

    #for each 3x3 box create a list of all the candidates in the box
    for y in candidatesBoxes:
        all_nums_in_box = []
        for x in y:
            all_nums_in_box += x

        #for each mini array of potential candidates for each 1x1 sudoku box, if a number in that mini array only occurs once
        #in the whole 3x3 box, then that number is the number that should be placed there in the final solution, so replace the
        #candidates mini array with an int which is that number
        sud_box_index = 0
        for candidates_in_sud_box in y:
            for num in candidates_in_sud_box:
                if(occurs_once(num, all_nums_in_box)):
                    y[sud_box_index] = [num]
            sud_box_index += 1

    return boxPacker(candidatesBoxes)

def check_for_zeros(sudoku_grid):
    solved = True
    for i in range(9):
        if 0 in sudoku_grid[i]:
            solved = False
    return solved

def insert_results(sudoku_grid, candidates):
    #takes an incomplete sudoku grid and a grid with candidate numbers, and fills the sudoku grid using the candidates info
    #returns the filled in sudoku grid, and also the updated candidates grid

    for i in range(9):
        for x in range(9):
            if(len(candidates[i][x]) == 1):
                sudoku_grid[i][x] = candidates[i][x][0]
                candidates[i][x] = []

    return [sudoku_grid, candidates]

easy = [
        [0, 4, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 3, 0, 7, 5, 0, 6, 0],
        [0, 0, 0, 2, 0, 0, 5, 4, 3],
        [0, 7, 2, 0, 0, 0, 0, 3, 9],
        [0, 0, 0, 9, 4, 2, 0, 0, 0],
        [5, 9, 0, 0, 0, 0, 6, 2, 0],
        [1, 2, 7, 0, 0, 3, 0, 0, 0],
        [0, 5, 0, 1, 9, 0, 2, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 7, 0],
       ]
hard = [
        [0, 5, 4, 0, 0, 0, 7, 0, 3],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 3, 7, 8, 5, 0, 0, 0, 4],
        [7, 0, 0, 0, 3, 4, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 1],
        [6, 0, 0, 0, 8, 7, 4, 2, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [5, 0, 2, 0, 0, 0, 6, 9, 0],
       ]
#v hard
inputGrid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [1, 0, 0, 8, 0, 0, 0, 0, 7],
        [0, 0, 6, 0, 9, 0, 5, 0, 3],
        [0, 9, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 5, 0, 0, 0, 4, 0, 0],
        [0, 0, 4, 7, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 6, 0, 4, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 2],
        [8, 3, 0, 0, 0, 5, 0, 9, 0],
       ]
inputGrid = [
        [0, 0, 0, 5, 0, 0, 1, 0, 0],
        [0, 0, 1, 2, 0, 0, 7, 6, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 8, 0, 0, 0, 3, 1, 0],
        [1, 0, 7, 0, 0, 0, 0, 4, 0],
        [0, 6, 5, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 1, 3, 0, 0, 7],
        [0, 0, 9, 0, 8, 6, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
       ]

# def solve(inputGrid):
    #copy the input so we can edit safely
finalGrid = inputGrid
count = 1
while check_for_zeros(finalGrid) == False and count < 10:
    candidates = findCandidates(inputGrid)
    candidates = scanning_solve(candidates)
    candidates = pointing_pairs_trimmer(candidates)
    finalGrid = insert_results(inputGrid, candidates)[0]
    print(finalGrid)
    print()
    count+=1

zeros = 0
for i in range(9):
    for x in range(9):
        if finalGrid[i][x] == 0:
            zeros += 1
print(finalGrid)
print(zeros)