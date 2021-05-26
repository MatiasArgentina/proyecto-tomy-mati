# Ternary Operators 
#  Ternary operators are more commonly known as conditional expressions

# value_if_true if condition else value_if_false

is_nice = False 
state = "nice" if is_nice else "not nice"
state

# Otro ejemplo con tupplas
# (if_test_is_false, if_test_is_true)[test]

nice = True 
personality = ("mean", "nice")[nice] #Porque TRUE es 1. 
print("The cat is ", personality)

#La primera opcion no evalua el False si no es necesario.
condition = True 
print(2 if condition else 1/0) 

#Para definir parametros opcionales
def my_function(real_name, optional_display_name = None): 
    final_value = optional_display_name or real_name
    print(final_value) 

my_function("John") 
my_function("Mike", "anonymous123")