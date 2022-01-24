# -*- coding: utf-8 -*-
'''
    :file: setup.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/01/24 14:54:39
'''
from os import path
from codecs import open
from setuptools import setup

basedir = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Flask-School',
    version='0.0.2',
    url='https://github.com/Farmer-chong/flask-school',
    license='MIT',
    author='farmer.chillax',
    author_email='farmer-chong@qq.com',
    description='School SDK extension with flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['flask_school'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask',
        'school-sdk'
    ],

    keywords='flask extension development',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)


# python setup.py bdist_wheel sdist
# twine upload dist/*
