from setuptools import setup, find_packages

setup(
    name='coauthorship-centrality',
    version='1.2.0',
    packages=find_packages(exclude=['internal']),
    url='',
    license='Apache 2.0',
    author='Victor',
    author_email='victor199704@gmail.com',
    description='A package used for computing node centrality in coauthorship networks.',
    install_requires=[
        "cycler==0.11.0",
        "fonttools==4.29.0",
        "kiwisolver==1.3.2",
        "matplotlib==3.5.1",
        "networkx==2.6.3",
        "numpy==1.22.1",
        "packaging==21.3",
        "pandas==1.4.0",
        "Pillow==9.0.0",
        "pyparsing==3.0.7",
        "python-dateutil==2.8.2",
        "pytz==2021.3",
        "scipy==1.7.1",
        "six==1.16.0",
    ]
)
