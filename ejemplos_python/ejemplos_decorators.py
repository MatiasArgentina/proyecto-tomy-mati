#Decorators 
# Decorators are a significant part of Python. In simple words: they are functions which modify the functionality of other functions. 
# Deco rators let you execute code before and after a function.

def hi(name="yasoob"): 
    return "hi " + name 
print(hi())

# We can even assign a function to a variable like 
greet = hi 
print(greet()) 

# Let's see what happens if we delete the old hi function! 
del hi 
print(hi()) 

print(greet()) #greet sigue siendo valida.

def hi(name="yasoob"): 
    print("now you are inside the hi() function") 
    def greet(): 
        return "now you are in the greet() function" 
    def welcome(): 
        return "now you are in the welcome() function" 
    print(greet()) 
    print(welcome()) 
    print("now you are back in the hi() function")

hi()
welcome() #Esta solo dentro de hi()

# Funciones devolviendo funciones
def hi(name="yasoob"): 
    def greet(): 
        return "now you are in the greet() function" 
    def welcome(): 
        return "now you are in the welcome() function" 
    if name == "yasoob": 
        return greet 
    else: 
        return welcome

hi('pepe')() #Devolvio una funcion.


# Giving a function as an argument to another function:
def hi(): 
    return "hi yasoob!" 
def doSomethingBeforeHi(func): 
    print("I am doing some boring work before executing hi()") 
    print(func()) 

doSomethingBeforeHi(hi) 

#Ejemplo practico:
def AbirConexion(Conn, ..., FuncionAEjecutar):
    #Abro la conexion
    FuncionAEjecutar()

# Writing your first decorator: 
def a_new_decorator(a_func): 
    def wrapTheFunction(): 
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()") 
    return wrapTheFunction 

def a_function_requiring_decoration(): 
    print("I am the function which needs some decoration to remove my foul smell") 

a_function_requiring_decoration() 

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration) 
#now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()

### Incompleto!