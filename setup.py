"""
aio.testing
"""
import os
from setuptools import setup, find_packages

version = "0.0.2"


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = read("README.rst")

setup(
    name='aio.testing',
    version=version,
    description="Asyncio testing utils",
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='',
    author='Ryan Northey',
    author_email='ryan@3ca.org.uk',
    url='http://github.com/phlax/aio.testing',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['aio'],
    include_package_data=True,
    zip_safe=False,
    test_suite="aio.testing.tests",
    install_requires=[
        'setuptools',
        ],
    entry_points="""
    # -*- Entry points: -*-
    """)
