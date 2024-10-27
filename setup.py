from setuptools import setup, find_packages

setup(
    name='your_module',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'your_command=your_module.cli:main',
        ],
    },
    install_requires=[
        # Your dependencies here
    ],
)