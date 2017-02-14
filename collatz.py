def collatz(number):
    if number %2 ==0:
        print(number//2)
        return number//2
    if number %2==1:
        print(3*number+1)
        return 3*number+1

print('PLease enter a number')
a=int(input())

b=collatz(a)

while b!=1:
    b=collatz(b)
    
