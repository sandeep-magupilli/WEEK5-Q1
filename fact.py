print("factorial without recursion ")

n=int(input("enter a number: "))

fact=1

for i in range(1,n+1):
    fact*=i
print("factorial of ",n,"is  without recursion: ",fact)

print("factorial with recursion:")

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print("factorial with recursion:",fact(n))

