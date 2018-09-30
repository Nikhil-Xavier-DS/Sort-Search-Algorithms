from setuptools import setup

setup(name='my_Sort',
      version='1.0',
      description='Search and Sort algorithms library',
      long_description='Library for Searching and Sorting Algorithms',
      author='Nikhil Xavier',
      author_email='nikhilxavier@yahoo.com',
      packages=['search_sort'],
      zip_safe=False,
      keywords='search sort algorithms',
      test_suite='nose.collector',
      tests_required=['nose'])