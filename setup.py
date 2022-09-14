from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="roliwrapper",
    version="2.1.0",
    author="htach",
    description="Rolimons API Wrapper",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/htach/roliwrapper",
    install_requires=["requests"],
    python_requires=">=3.9",
)
