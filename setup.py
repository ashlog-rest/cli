from setuptools import setup, find_packages
from ashlog.__meta__ import __version__

setup(
    name='ashlog',
    version=__version__,
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
