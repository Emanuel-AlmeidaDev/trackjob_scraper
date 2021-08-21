from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="trackjob_scraper",
    version="0.0.1",
    description="Extrator de dados de 'adm.trackjob.com.br em python",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Emanuel-AlmeidaDev/trackjob_scraper",
    author="Emanuel Almeida",
    author_email="emanuel_almeidadev@outlook.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    keywords="scraping - scraper",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.6",
    install_requires=["requests", "bs4"],
)