from setuptools import setup, find_packages

requirements = [
    'websocket-client>=0.32.0',
    'protobuf==3.5.0.post1',
    'six>=1.9.0',
]

setup(
    name="einplus_entryclient",
    author='EricPai <ericpai94@hotmail.com>',
    version='2.4.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
