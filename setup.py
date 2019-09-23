import os

from setuptools import setup, find_packages
from எண்ணிக்கை import உரைக்கு as உ

with open('نمونہ/تبدیل.txt', 'r', encoding='utf8') as تبدیل_کی_دستاویز:
    تبدیل = '.'.join(உ(ش, 'latin', 'ار') for ش in تبدیل_کی_دستاویز.read().strip().split('.'))

setup(
    name='namuna_panjab',
    version=تبدیل,
    packages=find_packages('/نمونہ'),
    download_url='https://github.com/julienmalard/namuna_panjab',
    license='GNU AFFERO GPL 3',
    author='محمّد اظہر انعام بیگ، ژولیئں ملاغ',
    author_email='julien.malard@mail.mcgill.ca; muhammad.baig@mail.mcgill.ca',
    description='',
    long_description='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    package_data={
        '': ['*.txt', '*.json' , '*.mdl', '.vpm'],
    },
    setup_requires=['ennikkai'],
)
