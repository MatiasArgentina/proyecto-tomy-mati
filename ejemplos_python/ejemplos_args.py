# *args para hacer funciones sin una cantidad de parametros predefinidos.

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg) 
    for arg in argv: 
        print("another arg through *argv:", arg) 

test_var_args('yasoob', 'python', 'eggs', 'test', 'test2')
test_var_args('yasoob')

# **kwargs
def greet_me(**kwargs): 
    for key, value in kwargs.items(): 
        print("{0} = {1}".format(key, value)) 

greet_me(name="yasoob", name2 = "Name!")

#Test
def test_args_kwargs(*arg1): 
    i = 1
    for arg in arg1:
        print("arg"+str(i)+":", arg)
        i =+ 1

args = ("two", 3, 5) 
test_args_kwargs(*args) #Tengo que llamarlo con el *
 
# now with **kwargs: 
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5} 
test_args_kwargs(**kwargs)

for name, arg in kwargs.items():
    print(name+":", arg)