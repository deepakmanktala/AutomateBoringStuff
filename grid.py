grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(len(grid))
print('Orignal diagram in question')

for i in range (0,9):
    for j in range(0,6):
        print(grid[i][j],end='')
    print('')
print('')    
print('Diagram as per Question-')
for i in range(0,6):
    for j in range(0,9):
        print(grid[j][i],end='')
    print('')   

print('')
print('Diagram as per fun')
for i in range(8,-1,-1):
    for j in range(5,-1,-1):
        print(grid[i][j], end='')
    print('')

print('')
print('Diagram as per fun part2')
for i in range (5,-1,-1):
    for j in range(0,9):
        print(grid[j][i],end='')
    print('')
