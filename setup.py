import os

from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="jet-sidebar",
    version="0.2.0",
    author="Raifran Lucas",
    author_email="contato@raifranlucas.dev",
    description="Este pacote é uma modificação para o Django Jet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raifran1/jet-sidebar",
    project_urls={
        "Bug Tracker": "https://github.com/raifran1/jet-sidebar/issues",
    },
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=2.6",
)