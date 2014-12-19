#!/usr/bin/env python3
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name='csv2sql',
    version='1.0.0',
    keywords='csv sql',
    url='https://github.com/tomleese/csv2sql',
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
        'console_scripts': ['csv2sql = csv2sql.__main__:main']
    },
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities'
    ],
    test_suite='tests'
)
