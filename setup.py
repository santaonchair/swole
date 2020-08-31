import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="swole",
    version="0.1",
    author="Nicolas REMOND",
    author_email="remondnicola@gmail.com",
    description="Short description of the package. TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astariul/swole",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
)
