import dis
from types import CodeType


def foo():
    print(2 + 2)


dis.dis(foo)
epilogue = f"Stacksize: {foo.__code__.co_stacksize}"
print("-" * len(epilogue))
print(epilogue)


# 1 + 2 and print the results
def bar():
    print(1 + 2)


def wrapper():
    bar()


dis.dis(wrapper)


needed_opcodes = ['LOAD_CONST', 'BINARY_ADD', 'LOAD_NAME', 'CALL_FUNCTION', 'POP_TOP', 'RETURN_VALUE']
for opcode_name in needed_opcodes:
    print(f"{opcode_name} -> {dis.opmap[opcode_name]}")

"""
LOAD_CONST -> 100
BINARY_ADD -> 23
LOAD_NAME -> 101
CALL_FUNCTION -> 131
POP_TOP -> 1
RETURN_VALUE -> 83
"""

bytecode = bytes([101, 0, 100, 0, 100, 1, 23, 0, 131, 1, 83, 0])

"""
CodeType(
        argcount,             #   integer
        kwonlyargcount,       #   integer
        nlocals,              #   integer
        stacksize,            #   integer
        flags,                #   integer
        codestring,           #   bytes
        consts,               #   tuple
        names,                #   tuple
        varnames,             #   tuple
        filename,             #   string
        name,                 #   string
        firstlineno,          #   integer
        lnotab,               #   bytes
        freevars,             #   tuple
        cellvars              #   tuple
        )
"""

codeobj = CodeType(
    0,  # argcount
    0,  # posonlyargcount
    0,  # kwonlyargcount
    0,  # nlocals
    3,  # stacksize
    64,  # flags (?)
    bytecode,  # codestring
    (1, 2),  # constants
    ('print',),  # names
    ('a',),  # varnames
    "<dummy>",  # filename
    "generated",
    1,  # firstlineno
    bytes([12, 1]),  # lnotab
    (),  # freevars
    (),  # cellvars
)

# print(foo.__code__.co_flags)


compiled = compile("print(1 + 2)", filename="dummy", mode='eval')
dis.dis(compiled)
print(list(compiled.co_code))
# print(compiled.co_varnames)
# print(compiled.co_consts)
# print(compiled.co_names)
# eval(compiled)

dis.dis(codeobj)
eval(codeobj)
# eval(compiled)

print(list(codeobj.co_linetable))
print(list(codeobj.co_lnotab))
print(list(compiled.co_linetable))
print(list(compiled.co_lnotab))

params = [
    "co_argcount",
    "co_posonlyargcount",
    "co_kwonlyargcount",
    "co_nlocals",
    "co_stacksize",
    "co_flags",
    "co_consts",
    "co_names",
    "co_varnames",
    "co_filename",
    "co_name",
    "co_firstlineno",
    "co_lnotab",
    "co_freevars",
    "co_cellvars",
]

for param in params:
    print(f"{param} - {getattr(codeobj, param)} - {getattr(compiled, param)}")

eval(codeobj)