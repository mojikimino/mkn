from setuptools import setup
from setuptools import find_packages

__name__ = "mkn"
__version__ = "0.0.2"

setup(
    name="mkn",
    version=__version__,
    description='A sample PyPI project',
    author="Moji Kimino",
    url="https://github.com/mojikimino/mkn",
    download_url="https://github.com/mojikimino/mkn/archive/{}.tar.gz".format(__version__),
    packages=["mkn"],
    include_package_data=True,
    install_requires=["pytest"]
)
