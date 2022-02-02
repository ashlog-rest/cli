from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='ashlog-cli',
    version='0.0.1',
    author='Giulio De Matteis',
    description='A simple command line interface for AshLog.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ashlog-rest/cli',
    project_urls={
        "Bug Tracker": "https://github.com/ashlog-rest/cli/issues",
    },
    package_dir={'': 'src'},
    packages=[
        'ashlog',
        'ashlog.commands',
        'common',
    ],
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
