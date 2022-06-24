import dis


#since dis.types.CodeType isnt very well documented I put a tiny script out to make leaked python bytecode easier to handle
#if you struggle with arguments in the eval see if you can get rid of them - ie not used in the actual bytecode
#MAKE SURE TO USE THE SAME PYTHON VERSION AS THE TARGET!!
#co_qualname NEEDS TO BE 0 - something isnt right with the order... too bad
#replace the values in the dictionary with your leaked values
#only use this if you are sure about what you are running

dictionary_of_leaked_code_objects = {'co_argcount': int(), 'co_posonlyargcount': int(), 'co_kwonlyargcount': int(), 'co_nlocals': int(), 'co_stacksize': int(), 'co_flags': int(), 'co_code': b'', 'co_consts': (), 'co_names': (), 'co_varnames': (), 'co_filename': '', 'co_name': '', 'co_qualname': 0, 'co_firstlineno': b''}


correct_order = ['co_argcount', 'co_posonlyargcount', 'co_kwonlyargcount', 'co_nlocals', 'co_stacksize', 'co_flags', 'co_code', 'co_consts', 'co_names', 'co_varnames', 'co_filename', 'co_name', 'co_qualname', 'co_firstlineno', 'co_linetable', 'co_exceptiontable', 'co_freevars', 'co_cellvars']


arguments = [dictionary_of_leaked_code_objects[i] for i in correct_order if i in dictionary_of_leaked_code_objects]


code = dis.types.CodeType(*arguments)

dis.dis(code)
eval(code)
