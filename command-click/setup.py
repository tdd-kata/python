from setuptools import setup, find_packages

setup(
    name="mark",
    version="0.1.0",
    author="markruler",
    description="Utility Commands",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    install_requires=[
        "click==8.1.3",
        "psutil==5.9.2",
    ],
    entry_points={"console_scripts": ["mark = mark.mark:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
