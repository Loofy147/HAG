from setuptools import setup, find_packages

setup(
    name="holographic-ai-governor",
    version="4.0.1",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "torch>=2.11.0",
        "pandas>=2.0.0",
        "kaggle>=1.5.12"
    ],
    entry_points={
        'console_scripts': [
            'hag-cli=src.cli.main:main',
        ],
    },
    author="loofy147",
    description="HAG-Desktop Build 4.0: Sovereign AI Desktop Agent System with LGA and RLM-N.",
    license="Sovereign Intelligence License",
    python_requires=">=3.8",
)
