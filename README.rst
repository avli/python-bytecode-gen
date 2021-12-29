python-bytecode-gen
===================

Compile stuff down to Python code objects.

::

    >>> from python_bytecode_gen.calc import gencode
    >>> codeobj = gencode("2 + 2")
    >>> eval(codeobj)
    4
    >>> # Incredible!
