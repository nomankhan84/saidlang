from setuptools import setup, find_packages

setup(
    name="saidlang",
    version="0.1.0",
    description="Ultra human-friendly programming language transpiled to Python",
    author="Said",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "said=saidlang.cli:main",
        ],
    },
    python_requires=">=3.8",
)
