from setuptools import setup, find_packages

install_requires = []

with open('requirements.txt', 'r', encoding='utf-8') as requirements_file:   
    install_requires = requirements_file.readlines()
      
setup(
    name='mrrf_library_one',
    version='1.0.0',
    author='Agent 1997',
    packages=find_packages(exclude=['docs']),
    install_requires=install_requires
)
