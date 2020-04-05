from setuptools import setup
from setuptools import find_packages

__name__ = "mkn"
__version__ = "0.0.1"

setup(
    name="mkn",
    version=__version__,
    description='A sample PyPI project',
    author="Moji Kimino",
    packages=["mkn"],
    include_package_data=True,
    install_requires=["pytest"]
)
