#!/usr/bin/env python3
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages


setup(
    name='csv2sql',
    version='1.0.0',
    keywords='csv sql converter',
    author='Tom Leese',
    author_email='inbox@tomleese.me.uk',
    url='https://github.com/tomleese/csv2sql',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['csv2sql = csv2sql.__main__:main']
    },
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities'
    ]
)
