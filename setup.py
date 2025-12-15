from setuptools import setup, find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
# this function will return list of requirements
def get_requirements(file_path:str)->list:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        


setup(
  name='ml_project1',
    version='0.0.1',
    author='Bhautik gondaliya',
    author_email='gondaliyabhautik419@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),

)