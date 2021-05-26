# set Data Structure 
# set is a really useful data structure. sets

#Encontrar duplicados sin set
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'] 
duplicates = [] 
for value in some_list: 
    if some_list.count(value) > 1: 
        if value not in duplicates: 
            duplicates.append(value) 

print(duplicates) 

#Encontrar duplicados con set
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates) 
[x for x in some_list if some_list.count(x) > 1] #esto deja muchas veces los duplicados

#Intersection 
valid = set(['yellow', 'red', 'blue', 'green', 'black', 'green', 'black']) 
input_set = set(['red', 'brown']) 
print(input_set.intersection(valid)) 

#Difference 
print(input_set.difference(valid)) 
input_set - valid

input_set.union(valid)
input_set | valid
