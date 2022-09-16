from setuptools import setup, find_packages

setup(
    name='pyssc',
    packages=find_packages(),
    version='0.0.1.dev2',
    license='MIT',
    author="jj-wohlgemuth",
    author_email='jj.wohlgemuth@gmail.com',
    url='https://github.com/jj-wohlgemuth/pyssc',
    keywords='Python Sennheiser Sound Control Protocol',
    install_requires=['zeroconf']
)
