import os
from typing import Dict

from setuptools import find_packages, setup

about: Dict[str, str] = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(
    os.path.join(here, "recipe_scrapers", "__version__.py"), "r", encoding="utf-8"
) as f:
    exec(f.read(), about)

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="recipe_scrapers",
    url="https://github.com/hhursev/recipe-scrapers/",
    version=about["__version__"],
    author="Hristo Harsev",
    author_email="r+pypi@hharsev.com",
    description="Python package, scraping recipes from all over the internet",
    keywords="python recipes scraper harvest recipe-scraper recipe-scrapers",
    long_description=README,
    long_description_content_type="text/x-rst",
    install_requires=[
        "beautifulsoup4>=4.10.0",
        "extruct>=0.8.0",
        "isodate>=0.6.1",
        "requests>=2.19.1",
        "types-beautifulsoup4>=4.11.6",
        "types-requests>=2.28.10",
    ],
    packages=find_packages(),
    package_data={"": ["LICENSE", "py.typed"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.6",
)
