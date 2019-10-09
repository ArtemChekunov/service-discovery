#!/usr/bin/env python

from setuptools import setup

setup(
    name='consul-sd',
    version='1.0.0',
    author='Javier Cacheiro, Artem Chekunov',
    author_email='artem.v.cherkunov@gmail.com',
    url='https://github.com/ArtemChekunov/service-discovery',
    license='MIT',
    description='Python client for Consul Service Discovery API',
    long_description=open('README.rst').read(),
    py_modules=['consul_sd'],
    install_requires=['requests'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
