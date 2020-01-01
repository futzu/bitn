import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitslicer9k",
    version="1.0.21",
    author="fu-corp",
    author_email="spam@futzu.com",
    description="Super Fast Bit Slicer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/futzu/bitslicer9k",
    #packages=setuptools.find_packages(),
    py_modules=['bitslicer9k'],
     platforms='all',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)
