from setuptools import setup, find_packages

def read_requirements(file):
    return [req.strip() for req in open(file).readlines()];

setup(
    name="app_entregas",
    version="1.0.0",
    description="App entregas",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
)