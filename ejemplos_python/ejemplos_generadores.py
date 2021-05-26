'''An iterable is any object in Python which has an __iter__ or 
a __getitem__ method defined which returns an iterator or can take 
indexes'''

'''An iterator is any object in Python which has a next (Python2) 
or __next__ method defined.''' 

'''Generators are iterators, but you can only iterate over them once.
It’s because they do not store all the values in memory, 
they generate the values on the fly'''

def generator_function(): 
    for i in range(10): 
        yield i 

generador = generator_function()
for item in generador: 
    if item < 5:
        print(item)
    else:
        print(item)
        break
next(generador)

generador = generator_function()
next(generador)

# generator version 
def fibon(n): 
    a = b = 1 
    for i in range(n): 
        yield a 
        a, b = b, a + b

for x in fibon(10): 
    print(x)

def generator_function(): 
    for i in range(3): 
        yield i 
gen = generator_function()

print(next(gen))

#Errores porque son iterables pero no iteradores.
my_string = "Yasoob" 
next(my_string) 
int_var = 1779 
iter(int_var) 

my_string = "Yasoob" 
my_iter = iter(my_string) 
print(next(my_iter)) 

