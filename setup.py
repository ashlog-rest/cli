from setuptools import setup, find_packages
from ashlog.__meta__ import __version__

setup(
    name='ashlog-cli',
    version=__version__,
    author='Giulio De Matteis',
    description='A simple command line interface for AshLog.',
    url='https://github.com/ashlog-rest/cli',
    project_urls={
        "Bug Tracker": "https://github.com/ashlog-rest/cli/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'keyring',
        'pyyaml',
        'requests',
    ],
    entry_points={
        'console_scripts': ['ashlog=ashlog.cli:cli']
    }
)
