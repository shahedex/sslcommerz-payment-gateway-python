import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'astroid==2.3.3',
    'certifi==2019.11.28',
    'chardet==3.0.4',
    'idna==2.8',
    'isort==4.3.21',
    'lazy-object-proxy==1.4.3',
    'mccabe==0.6.1',
    'requests==2.22.0',
    'six==1.13.0',
    'typed-ast==1.4.0',
    'urllib3==1.25.7',
    'wrapt==1.11.2'
]

setuptools.setup(
    name="sslcommerz-python",
    version="0.0.5",
    author="Shahed Mehbub",
    author_email="shahed739@gmail.com",
    description="Implements SSLCOMMERZ payment gateway in python based web apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahedex/sslcommerz-payment-gateway-python",
    packages=setuptools.find_packages(),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)