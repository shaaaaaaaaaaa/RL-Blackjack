from setuptools import setup

setup(
    name="gym_examples",
    version="0.0.1",
    install_requires=["gymnasium==0.29.1", "pygame==2.1.0"],
    packages=["gym_examples", "gym_examples.envs"],
)
