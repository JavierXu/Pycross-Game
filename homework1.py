# Yaozhong Xu

# start time calculation
import datetime 
x = datetime.datetime.now()

# use layout program to generate square boards
import layout 
print(layout.rows, layout.columns)
eof = [layout.marker.full,layout.marker.empty]
master = []
scratch = []

# use random to generate filled cells in masterboard
import random  
for i in range(layout.rows):
    master.append([])
    for j in range(layout.columns):
        master[i].append(eof[random.randint(0,1)])

# generate scratch board
for i in range(layout.rows):
    scratch.append([])
    for j in range(layout.columns):
        scratch[i].append(eof[1])

# count the (*)s in master board
tfn = 0
for i in master:
    tfn = tfn + i.count("*")

# count the number of stars in rows
tomorow = []
for i in master:
    filledrow = 0
    pos = []
    for j in i:
        if j == eof[0]:
            filledrow = filledrow + 1
        elif filledrow > 0:
            pos.append(str(filledrow))
            filledrow = 0
    if filledrow > 0:
        pos.append(str(filledrow))
        filledrow = 0
    tomorow.append(pos)

# swap the list so that I can count stars in columns
collist = []
for i in master:
    collist.append(i.copy())
for i in range(len(master)):
    row = master[i]
    for j in range(len(row)):
        collist[j][i] = master[i][j]

# count the stars in columns
tomocol = []
for i in collist:
    filledcol = 0
    pos = []
    for j in i:
        if j == eof[0]:
            filledcol = filledcol + 1
        elif filledcol > 0:
            pos.append(str(filledcol))
            filledcol = 0
    if filledcol > 0:
        pos.append(str(filledcol))
        filledcol = 0
    tomocol.append(pos)
    
# make the lists in tomocol have the same length
tomocolswap = []
for i in tomocol:
    for j in range(layout.columns-len(i)):
        i.append(" ")
    tomocolswap.append(i)

# swap the list of counted numbers in columns so that I can append it below
# the scratch board
swapcollist = []
for i in tomocolswap:
    swapcollist.append(i.copy())
for i in range(len(tomocolswap)):
    row = tomocolswap[i]
    for j in range(len(row)):
        swapcollist[j][i] = tomocolswap[i][j]

# print the scratch board
row_length = len(scratch[0])
separator = (layout.board.corner + layout.board.top) * row_length + '+'
print(separator)

# print the numbers behind the rows
v =0
for sublist in scratch:
    row = layout.board.side
    for i in sublist:
        row += i + layout.board.side
    print(row, end=' ')
    print(" ".join(tomorow[v]))
    v = v+1
    print(separator)
  
# print the numbers below the columns
k = 0
while k < layout.columns:
    print(" " + " ".join(swapcollist[k]))
    k = k + 1

# ask coordinates from the users for interaction and play the games
j = 0
guess = 0
while j < tfn:
    coordinates = input("Please enter your guess: row, col").split(",")
    row = int(coordinates[0])
    col = int(coordinates[1])
    guess = guess + 1
    # check whether the guess is right
    if row < layout.rows and col < layout.columns:
        if master[row][col] == eof[0]:
            scratch[row][col] = eof[0]
            print(separator)
            j = j + 1
        else:
            continue
        # repeat printing the scratch board
        v=0
        for sublist in scratch:
            row = layout.board.side
            for i in sublist:
                row += i + layout.board.side
            print(row, end = ' ')
            print(" ".join(tomorow[v]))
            v =v+1
            print(separator)  
        k = 0
        while k < layout.columns:
            print(" " + " ".join(swapcollist[k]))
            k = k + 1
    else:
        continue
# game finished
guess_accuracy = tfn/guess
print("Your guess accuracy is " + str(guess_accuracy))
y = datetime.datetime.now()
print("The game duration is " + str(y - x))
