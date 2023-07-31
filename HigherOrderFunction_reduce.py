#calculate the sum of numbers in the list
import functools
lis=[12,34,56,78,45]
a=functools.reduce(lambda x,y:x+y,lis)
print(a)

#find the maximum number in the list
lis=[12,34,56,78,45]
print(functools.reduce(lambda x,y:x if x>y else y,lis))

#find the minimum number in the list
lis=[12,34,56,78,45]
print(functools.reduce(lambda x,y:x if x<y else y,lis))