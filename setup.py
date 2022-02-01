from setuptools import setup, find_packages

setup(
    name='ashlog-cli',
    version='0.0.1',
    author='Giulio De Matteis',
    description='A simple command line interface for AshLog.',
    url='https://github.com/ashlog-rest/cli',
    project_urls={
        "Bug Tracker": "https://github.com/ashlog-rest/cli/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
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
