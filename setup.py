import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pwgen_secure",
    version="0.9.0",
    author="Michael Munger",
    author_email="mj@hph.io",
    description="Generate cryptographically secure random passwords with specified character sets, patterns, or lengths.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mjmunger/pwgen_secure",
    packages=setuptools.find_packages(),
    classifiers=[
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Development Status :: 5 - Production/Stable',
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
