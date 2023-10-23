from setuptools import setup, find_packages

setup(
    name='safescript',
    version='1.0.1',
    description='A Python module for enhancing web application security',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ishan Oshada',
    author_email='ic31908@gmail.com',
    url='https://github.com/ishanoshada/safescript',
    packages=find_packages(),
    install_requires=[
        # Add any required dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
