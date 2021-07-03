import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jet-sidebar",
    version="0.0.1",
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
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "jet_sidebar"},
    packages=setuptools.find_packages(where="jet_sidebar"),
    python_requires=">=2.6",
)