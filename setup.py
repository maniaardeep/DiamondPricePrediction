from setuptools import setup, find_packages

def read_requirements():
    """Reads dependencies from requirements.txt and returns them as a list."""
    with open("requirements.txt", encoding="utf-8") as f:
        return f.read().splitlines()

setup(
    name='mypackage',  # Name of the package
    version='0.1',  # Package version
    description='A short description of my package',  # Short description
    long_description=open("README.md", encoding="utf-8").read(),  # Long description from README
    long_description_content_type="text/markdown",  # Content type of long description
    author='Your Name',  # Author name
    author_email='your.email@example.com',  # Author email
    url='https://github.com/yourusername/mypackage',  # URL of the project (e.g., GitHub link)
    packages=find_packages(),  # Automatically finds sub-packages
    install_requires=read_requirements(),  # Reads dependencies from requirements.txt
    classifiers=[  # Metadata about the package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
