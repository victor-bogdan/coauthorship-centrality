from setuptools import setup, find_packages

setup(
    name='coauthorship-centrality',
    version='0.1.0',
    packages=find_packages(),
    url='',
    license='Apache 2.0',
    author='Victor',
    author_email='victor199704@gmail.com',
    description='A package used for computing node centrality in coauthorship networks',
    install_requires=[
        "numpy==1.23.0",
        "pandas==1.4.2",
        "python-dateutil==2.8.2",
        "pytz==2022.1",
        "six==1.16.0",
    ]
)
