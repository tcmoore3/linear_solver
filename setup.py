from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

requirements = [line.strip() for line in open('requirements.txt').readlines()]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(['linear_solver'])
        sys.exit(errcode)


setup(name='linear_solver',
      version='0.0',
      description='',
      url='http://github.com/tcmoore3/linear_solver',
      author='Timothy C. Moore',
      author_email='timothy.c.moore@vanderbilt.edu',
      license='MIT',
      packages=['linear_solver'],
      install_requires=requirements,
      zip_safe=False,
      test_suite='tests',
      cmdclass={'test': PyTest},
      extras_require={'utils': ['pytest']},
)
