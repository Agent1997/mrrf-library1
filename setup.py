import logging
from setuptools import setup, find_packages

install_requires = []

try:
    with open('requirements.txt', 'r', encoding='utf-8') as requirements_file:
        install_requires = requirements_file.readlines()
except Exception:
    logging.warning("Exception raised when attempting to read the requirements.txt using utf-8 encoding.")
    logging.warning("Retry reading requirements.txt using utf-16 encoding")
    with open('requirements.txt', 'r', encoding='utf-16') as requirements_file:
        install_requires = requirements_file.readlines()


# Since the content of the requirements.txt is a url of another github repo, we will add the content
# as a dependency link instead. See: https://python-packaging.readthedocs.io/en/latest/dependencies.html#packages-not-on-pypi

# In cases where requirements.txt has also dependencies from pypi like selenium==4.9.1, better to put them in separate files
# Read and add them separately in setup.py as install_requires and dependency_links. When setting up workspace
# for the project where dependencies are in multiple text files, be sure to install all of those using 
# pip install -r <filename> . 
# E.g. 
#       pip install - requirements.txt      
#       pip install  dependencylinks.txt
setup(
    name='mrrf_library_one',
    version='1.0.0',
    author='Agent 1997',
    packages=find_packages(exclude=['docs']),
    install_requires=install_requires
)
