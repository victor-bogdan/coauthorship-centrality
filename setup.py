from setuptools import setup, find_packages

setup(
    name='coauthorship-centrality',
    version='1.4.0',
    packages=find_packages(exclude=['internal']),
    url='',
    license='Apache 2.0',
    author='Victor',
    author_email='victor199704@gmail.com',
    description='A package used for computing node centrality in coauthorship networks.',
    install_requires=[
        "contourpy==1.2.0",
        "cycler==0.12.1",
        "fonttools==4.44.0",
        "importlib-resources==6.1.0",
        "kiwisolver==1.4.5",
        "matplotlib==3.8.1",
        "networkx==2.6.3",
        "numpy==1.26.1",
        "packaging==23.2",
        "pandas==1.4.4",
        "Pillow==10.1.0",
        "pyparsing==3.1.1",
        "python-dateutil==2.8.2",
        "pytz==2023.3.post1",
        "scipy==1.11.3",
        "six==1.16.0",
        "zipp==3.17.0"
    ]
)
