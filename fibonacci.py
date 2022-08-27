n=int(input("Enter the number "))
# Set count
i=0
j=1
count=0
# if number is less then 0
if n<0: print("Enter positive number")
# if number is equal to 1
if n==1: print("Fibonacci sequence is",i)
else : print("Fibonacci series: ")
while count<n:
    print(i)
    nth=i+j
    i=j
    j=nth
    count+=1
