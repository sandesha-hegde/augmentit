import setuptools


with open('requirements.txt') as f:
    required = f.read().splitlines()


setuptools.setup(
    name="augmentit",
    version="1.0.2",
    author="Sandesh Hegde",
    author_email="sandesh.hegde@camcom.com",
    description="A small package to do some augmentation",
    url="https://gitlab.com/sandesha/augmentit.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
)

# python3 -m twine upload --repository gitlab dist/*