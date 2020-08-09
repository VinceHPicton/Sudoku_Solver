class FindCandidates:
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