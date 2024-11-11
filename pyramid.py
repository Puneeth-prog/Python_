rows = 11  #number rows required

k = 0                                         # initializing the column to 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print(k , end=" ")
        k += 1                                 #increase the number count

    k = 0                                      #again start printing from 0
    print()
