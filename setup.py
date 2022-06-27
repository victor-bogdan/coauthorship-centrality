from setuptools import setup, find_packages

setup(
    name='coauthorship-centrality',
    version='0.1.0',
    packages=find_packages(exclude=['internal']),
    url='',
    license='Apache 2.0',
    author='Victor',
    author_email='victor199704@gmail.com',
    description='A package used for computing node centrality in coauthorship networks',
    install_requires=[
        "networkx==2.6.3",
        "numpy==1.22.1",
        "pandas==1.4.0",
        "python-dateutil==2.8.2",
        "pytz==2021.3",
        "six==1.16.0",
    ]
)
