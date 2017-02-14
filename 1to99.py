print('input highest Number')
highest=int(input())
print('input Lowest Number')
Lowest=int(input())
print('input a divisor')
divisor=int(input())
spam=[]
for j in range(Lowest,highest):
    j/=divisor
    '''print(int(j))'''
    spam=spam+[int(j)]

print(spam)

