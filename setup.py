# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ciscocsraxl',
    version='0.1.0',
    description='Cisco CSR AXL',
    long_description=readme,
    author='Carlos Sanz',
    author_email='carlos.sanz@gmail.com',
    url='https://github.com/sanzcarlos/Cisco_CSR_AXL',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)