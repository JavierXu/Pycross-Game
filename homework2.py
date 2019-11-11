def get_board(csvfile):
    fp = open(csvfile)
    biglist = []
    for line in fp:
        row = line.strip().split(',')
        biglist.append(row)
    return biglist
            