#using list comprehension double the element of list
lis=[1,2,3,4,5]
print([item*2 for item in lis])

#print the square of numbers upto 10
print([i**2 for i in range(10)])

#print the square of odd numbers upto 10
print([i**2 for i in range(10) if i % 2!=0])

#print the square of even numbers upto 10
print([i**2 for i in range(10) if i % 2==0])

#print those fruits whose name  contains 'e'
fruits=['Apple','Mango','Orange','Guava']
print([fruit for fruit in fruits if 'e' in fruit])

#print those fruits whose name starts with 'O'
fruits=['Apple','Mango','Orange','Guava']
print([fruit for fruit in fruits if fruit[0] == 'O'])

#print those key value pairs in which length of key >3
D={"Name":"Ashu","Gender":"Male","Age":22}
D1={key:value for key,value in D.items() if len(key)>3 }
print(D1)