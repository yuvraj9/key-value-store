import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="key-value-store",
    version="0.0.1",
    author="Yuvraj Singh Shekhawat",
    author_email="shekhawatyuvraj1998@gmail.com",
    description="Key value store",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuvraj9/kv-value-store",
    project_urls={
        "Bug Tracker": "https://github.com/yuvraj9/kv-value-store/issues",
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    packages=setuptools.find_packages(exclude=['tests*'])
)