import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitn",
    version="0.0.29",
    author="fu-corp",
    author_email="spam@futzu.com",
    description="Bitwise Bit Slicing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/bitn",
    py_modules=['bitn'],
     platforms='all',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)
