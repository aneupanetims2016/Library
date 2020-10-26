import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Library",
    version="0.0.1",
    author="Archana Neupane Timsina",
    author_email="aneupanetims2016@fau.edu",
    description="Import everything used in the MPCR lab.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/aneupanetims2016/Library",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
