from setuptools import setup, find_packages

setup(
    name="python-bytecode-gen",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'parser = calc.parser:main',
        ],
    },
)
