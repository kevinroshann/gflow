from setuptools import setup, find_packages

setup(
    name="gflow",
    version="1.0.0",
    description="A CLI to simplify multi-step Git workflows",
    author="Kevin",
    author_email="your@email.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["typer"],
    entry_points={
        "console_scripts": [
            "gflow=gflow.main:app"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
