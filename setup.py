import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitn",
    version="0.0.43",
    author="fu-corp",
    author_email="spam@futzu.com",
    description="Bit Wise Slicing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/bitn",
    py_modules=["bitn"],
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires=">=3.6",
)
