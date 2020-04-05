from setuptools import setup
from setuptools import find_packages

__name__ = "mkn"
__version__ = "0.0.1"

setup(
    name=__name__,
    version=__version__,
    description='A sample PyPI project',
    author="Moji Kimino",
    packages=find_packages(where="mkn"),
    install_requires=["pytest"]
)
