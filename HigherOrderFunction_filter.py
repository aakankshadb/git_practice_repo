#iterate through the list and print only those valuse which are greater than 4
lis = [1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x>4,lis)))

#iterate through th list and print those fruits whose name contain e
fruits = ["Apple","orange","banana","guava"]
print(list(filter(lambda x:'e' in x,fruits)))
