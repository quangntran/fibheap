
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fibheap",
    version="0.2.1",
    author="Quang Tran",
    author_email="quang.tran@minerva.kgi.edu",
    description="An implementation of Fibonacci heap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quangntran/fibheap.git",
    packages=['fibheap'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
#
# import io
# import os
# import sys
# from setuptools import setup
#
# here = os.path.abspath(os.path.dirname(__file__))
#
# DESCRIPTION = "Fibheap"
#
# try:
#     with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
#         long_description = f.read()
# except FileNotFoundError:
#     long_description = DESCRIPTION
#
# setup(name='fibheap',
#       version='0.1.7',
#       description="fibheap",
#       long_description=long_description,
#       long_description_content_type='text/markdown',
#       url='https://github.com/quangntran/fibheap',
#       author='Quang Tran',
#       author_email='quang.tran@minerva.kgi.edu',
#       license='MIT',
#       classifiers=[
#           "Programming Language :: Python :: 3",
#           "License :: OSI Approved :: MIT License",
#           "Operating System :: OS Independent",
#       ],
#       packages=['fibheap'],
#       )
