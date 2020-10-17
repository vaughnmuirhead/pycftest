import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycftest",
    version="0.6",
    author="Vaughn Muirhead",
    author_email="vaughn.muirhead@gmail.com",
    description="A package to assist with writing unit tests for Google Cloud Functions written in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaughnmuirhead/pycftest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License Version 2.0",
        "Operating System :: OS Independent",
    ],
)
