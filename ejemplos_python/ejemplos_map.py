# Map, Filter and Reduce   

#Map applies a function to all the items in an input_list.
#map(function_to_apply, list_of_inputs)

#Solucion sin Map
items = [1, 2, 3, 4, 5] 
squared = [] 
for i in items: 
    squared.append(i**2)
squared

#Con Map
items = [1, 2, 3, 4, 5] 
squared = list(map(lambda x: x**2, items))
squared

#Con Map donde defino los argumentos y 
# se los paso a una lista de funciones.
def multiply(x): 
    return (x*x) 
def add(x): 
    return (x+x) 
funcs = [multiply, add] 
for i in range(5): 
    value = list(map(lambda x: x(i), funcs)) 
    print(value)

#Filter
#Filtrar una lista por condiciones
number_list = range(-5, 5) 
less_than_zero = list(filter(lambda x: x < 0, number_list)) 
print(less_than_zero) 

#Reduce 
# Sin Reduce
product = 1 
list = [1, 2, 3, 4] 
for num in list: 
    product = product * num 
product
#Reduce - It applies a rolling computation to sequential pairs of values in a list.
from functools import reduce 
product = reduce((lambda x, y: x * y), [2, 3, 5]) 
product