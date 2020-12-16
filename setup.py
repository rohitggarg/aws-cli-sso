import os
import setuptools

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name = "aws-cli-sso",
    version = "0.0.1",
    author = "Rohit Garg",
    author_email = "rohitgarg19@gmail.com",
    description = ("A tool that you can use to SSO and reload aws session in credentials file."),
    license = "MIT",
    keywords = "aws sso saml auth assume role sts",
    url = "http://packages.python.org/aws-cli-sso",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
        'boto3'
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
)
