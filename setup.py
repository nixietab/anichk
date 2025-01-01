from setuptools import setup, find_packages

setup(
    name='AniChk',
    version='1.0.0',
    description='A tool to generate phrases based on file or directory checksum',
    author='Nixietab',
    url='https://github.com/nixietab/anichk',
    packages=find_packages(),
    py_modules=['anichk'],
    entry_points={
        'console_scripts': [
            'anichk = anichk:main',
        ],
    },
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    package_data={
        'anichk': ['adjetive.txt', 'animal.txt'],
    },
)
