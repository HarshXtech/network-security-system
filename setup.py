"""

Configurations of the project such as - metadata, dependencies, versions, and more.

"""

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            for line in lines:
               requirements = line.strip()
               # ignore empty lines and -e.
               if requirements and requirements != '-e .':
                   requirement_lst.append(requirements)
    except FileNotFoundError:
        print('requirements.txt file not found!')

setup(
    name = "Network security system",
    version='0.0.1',
    author = "Harsh Gadhiya",
    author_email= "harshgadhiya08@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(),
) 