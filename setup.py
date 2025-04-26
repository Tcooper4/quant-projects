from setuptools import setup, find_packages

setup(
    name='quant_projects',
    version='0.1',
    package_dir={'': 'src'},  # <--- TELL IT TO LOOK INSIDE src/
    packages=find_packages(where='src'),  # <--- FIND PACKAGES INSIDE src/
)
