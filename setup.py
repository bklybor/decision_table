from setuptools import setup

setup(name='decision_table',
      version='0.1',
      description='a simple implementation of a decision table',
      url='http://github.com/bklybor/decision_table',
      author='Benjamin Klybor',
      author_email='bklybor@gmail.com',
      license='MIT',
      packages=['decision_table'],
      install_requires=[
          'tabulate',
      ],
      zip_safe=False)