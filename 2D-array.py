array = []
for a in range(6):
    Input = [int(x) for x in str(input()).split(' ')]
    array.append(Input)
maximum = -9*7
for i in range(6):
    for j in range(6):
        if i + 2 < 6 and j + 2 < 6:
            res = array[i][j]+array[i][j+1]+array[i][j+2]+array[i+1][j+1]+array[i+2][j]+array[i+2][j+1]+array[i+2][j+2]
            if res>maximum:
                maximum = res
print(maximum)