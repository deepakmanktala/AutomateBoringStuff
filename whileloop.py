while True:                         # (1)
    print('Please type your name.')
    name = input()                  # (2)
    if name == '':         # (3)
        break                       # (4)
print('Thank you!')


name = ''                           # (1)
while name != 'your name':          # (2)
    print('Please type your name.')
    name = input()
    if len(name) == 2:
        break# (3)
print('Thank you!')    
