from heapq import heappush, heappop

def quickestWayUp(ladders, snakes):
    mindistance = [float('inf') for i in range(101)]
    laddersSnakes = [0 for i in range(101)] # Only need one list for snakes and ladders
    for head, tail in ladders + snakes:
        laddersSnakes[head] = tail 

    queue = [(1, 0)]
    while queue:
        square, moves = heappop(queue)
        for a in range(1, 7):
            try:
                newSquare = square + a
                if laddersSnakes[square + a] != 0: # checks if there is a snake or ladder
                    newSquare = laddersSnakes[square + a] 
                if moves + 1 < mindistance[newSquare]:
                    mindistance[newSquare] = moves + 1
                    heappush(queue, (newSquare, moves + 1))
            except: 
                break
    return -1 if mindistance[100] == float('inf') else mindistance[100]
