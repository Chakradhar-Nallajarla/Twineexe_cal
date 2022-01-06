from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="chakri3-twine",
    version="3.0.9",
    description="A Python package to get weather reports for any location.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Chakradhar-Nallajarla/Twine-.git",
    author="Chakradhar Nallajarla",
    author_email="chakradharnallajarla@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["chakri3_twine"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "chakri3-twine=chakri3_twine.cli:main",
        ]
    },
)