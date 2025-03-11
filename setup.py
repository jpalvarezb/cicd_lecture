from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    lines = f.readlines()

reqs = [package.strip() for package in lines if '#' not in package]

setup(name='cicd',packages=find_packages(), install_requires=reqs)
