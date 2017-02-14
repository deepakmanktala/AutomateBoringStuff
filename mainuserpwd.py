print('Enter Name')
name = raw_input()

if name == 'Mary':
    print('Hello Mary')
    print('Enter Password')
    password = raw_input()
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
else:
    print('Wrong Username.')
