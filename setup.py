import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi7db", 
    version="0.4.8",
    author="Shivjeet Singh Bhullar",
    author_email="bhullarshivjeet@gmail.com",
    description="pi7db Is A Fast And Powerfull Directory Based Database Built In Python3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivjeetbhullar/pi7db",
    packages=setuptools.find_packages(),
    install_requires=["pycryptodome"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Database"
    ],
    python_requires='>=3.6',
)
