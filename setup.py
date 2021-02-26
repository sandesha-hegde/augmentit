import setuptools


with open('requirements.txt') as f:
    required = f.read().splitlines()


setuptools.setup(
    name="augmentit",
    description= "package to do some basic image augmentation for polygons and boxes.",
    version="1.0.3",
    author="Sandesh Hegde",
    author_email="sandeshangiras@gmail.com",
    url="https://github.com/sandesha-hegde/augmentit.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
)

# python3 -m twine upload --repository gitlab dist/*
# python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*