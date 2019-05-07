# coding:utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demo_grpc",
    version="0.0.1",
    author="wangjie",
    author_email="wangjie02@megvii.com",
    description="A grpc demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangjie07/grpc_demo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    install_requires=[
        "grpcio==1.19.0",
        "protobuf==3.7.1",
        "grpcio-tools==1.19.0"
    ]
)