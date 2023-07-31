# Write a logic to return three output from a function which
#will take arguments as function as well as list:
#even numbers from the list
#odd numbers from the list
#numbers divisble by
lis=[11,14,21,23,56,78,45,29,28]

x=lambda x:x%2==0
y=lambda x:x%2!=0
z=lambda x:x%3==0

def return_sum(func,L):
    result=0
    for i in L:
        if func(i):
            result=result+i
    return result

print("Sum of even number is",return_sum(x,lis))
print("Sum of odd number is",return_sum(y,lis))
print("Sum of number divisible by 3 is",return_sum(z,lis))