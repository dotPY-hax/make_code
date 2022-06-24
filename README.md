# make_code
making usage of leaked python __code__ objects easier

since dis.types.CodeType isnt very well documented I put a tiny script out to make leaked python bytecode easier to handle

if you struggle with arguments in the eval see if you can get rid of them - ie not used in the actual bytecode

MAKE SURE TO USE THE SAME PYTHON VERSION AS THE TARGET!!

co_qualname NEEDS TO BE 0 - something isnt right with the order... too bad

replace the values in the dictionary with your leaked values

only use this if you are sure about what you are running
