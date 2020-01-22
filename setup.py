import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pathogen_memo", # Replace with your own username
    version="1.1.1",
    author="NajlaBioinfo",
    author_email="bhnajla.bi@outlook.com",
    description="A small web application displaying friendly somes pathogen characteristics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NajlaBioinfo/pathogen_memo_app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

