from rand import random

#Testing our random function by giving min , max limit and getting output as list and then compute percentage of higher number for reference
print('Enter min limit')
min = int(input())
print('Enter max limit')
max = int(input())
while max < min:
    print('Wrong max limit\nEnter Again: ')
    max = int(input())
print('Want to generate more than one number input Y')
ch = input()
n = 1
if ch == 'Y' or ch == 'y':
    print("input number of random no. you want to generate")
    n = int(input())
res = random(min,max,n)
print('random numbers are :- ',res,sep='\n',end='\n')
greater = [x for x in res if x > min+((max-min)/2)]
print('percentage of higher numbers out of n =',n,' is ',len(greater)/n*100)