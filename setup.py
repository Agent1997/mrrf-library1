from setuptools import setup, find_packages
   
setup(
    name='mrrf_library_one',
    version='1.0.0',
    author='Agent 1997',
    packages=find_packages(exclude=['docs']),
    dependency_links=["git+https://github.com/Agent1997/mrrf-core.git@main"]
)
