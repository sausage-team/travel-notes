import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

setup(
    name="mysite",
    version="0.1",
    packages=find_packages(),
    include_package_data = True,
    exclude_package_data = {'':['.DS_Store']},
    license = 'BSD License',
    description = "A simple Django app",
    long_description=README,
    url='https://www.example.com/',
    author='tangdaoyuan',
    author_email='1197633750@qq.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
