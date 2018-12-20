import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fibheap",
    version="0.0.1",
    author="Quang Tran",
    author_email="quangtran0698@gmail.com",
    description="An implementation of Fibonacci heap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quangntran/fibheap.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
