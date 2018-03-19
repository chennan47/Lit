#1D solutioin
def game_of_life_1d(arr):
    n = len(arr)

    for x in range(n):
        live_count = 0
        if arr[(x+1+n) % n] & 1 == 1:
            live_count += 1
        if arr[(x-1+n) % n] & 1 == 1:
            live_count += 1

        if live_count == 1:
            arr[x] *= (arr[x] + 1) % 2 * 2
        else:
            arr[x] += arr[x] * 2

    for x in range(n):
        arr[x] >>= 1

# This is 2D solution. Ask about cross border situation.

def game_of_life_2d(grid):
    m, n = len(grid), len(grid[0])

    for x in range(m):
        for y in range(n):
            live_count = get_live_count(grid, x, y, m, n)

            #  print x, y, live_count
            if grid[x][y] == 1:
                if live_count == 2 or live_count == 3:
                    grid[x][y] += 2
            elif live_count == 3:
                grid[x][y] += 2

    for x in range(m):
        for y in range(n):
            grid[x][y] >>= 1


# Ask. Be clear about this.
def get_live_count(grid, x, y, m, n):
    live_count = 0
    if grid[x][(y+1+n) % n] & 1 == 1:
        live_count += 1
    if grid[x][(y-1+n) % n] & 1 == 1:
        live_count += 1

    if grid[(x+1+m) % m][y] & 1 == 1:
        live_count += 1
    if grid[(x-1+m) % m][y] & 1 == 1:
        live_count += 1

    if grid[(x+1+m) % m][(y+1+n) % n] & 1 == 1:
        live_count += 1
    if grid[(x+1+m) % m][(y-1+n) % n] & 1 == 1:
        live_count += 1

    if grid[(x-1+m) % m][(y+1+n) % n] & 1 == 1:
        live_count += 1
    if grid[(x-1+m) % m][(y-1+n) % n] & 1 == 1:
        live_count += 1

    return live_count


# cur_generation = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
# ctr = collections.Counter((I, J)
#                                          for i, j in live
#                                          for I in range(i-1, i+2)
#                                          for J in range(j-1, j+2)
#                                          if I != i or J != j)
#
# next_generation = {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}