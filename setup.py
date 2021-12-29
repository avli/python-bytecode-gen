from setuptools import setup, find_packages

setup(
    name="Python Bytecode Generation",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'parser = python_bytecode_gen.calc.parser:main',
        ],
    },
)
