import pdb 

a = 33

def make_bread(a): 
    pdb.set_trace() 
    return "I don't have time" 

print(make_bread(23))


#Commands: 
##c: continue execution 
##w: shows the context of the current line it is executing. 
##a: print the argument list of the current function 
##s: Execute the current line and stop at the first possible occasion. 
##n: Continue execution until the next line in the current function is reached or it returns. 