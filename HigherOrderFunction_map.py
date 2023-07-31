#iterate through the list and double each element of list
lis=[1,2,3,4,5,90]
print(list(map(lambda x:x*2,lis)))

#iterate through list and check each element is even or odd
print(list(map(lambda x:x%2 == 0,lis)))

#iterate through list of dictionary and print the name from each element
students=[
    {"name":"Jacob Martin",
    "father name":"Ros Martin",
     "Address":"123 Hill Street"
    },
    {"name":"Angela Stevens",
    "father name":"Robert Stevens",
     "Address":"3 Upper Street London"
     },
    {"name":"Ricky Smart",
    "father name":"William Smart",
     "Address":"Unknown"
     }
]
print(list(map(lambda student:student["name"],students)))



