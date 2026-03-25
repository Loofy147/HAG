from setuptools import setup, find_packages

setup(
    name="holographic-ai-governor",
    version="2.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "torch>=2.0.0",
        "pandas>=2.0.0",
        "kaggle>=1.5.12"
    ],
    author="hichambedrani",
    description="A sovereign AI system with holographic weight encoding and symmetry-aware learning.",
    license="Sovereign Intelligence License",
    python_requires=">=3.8",
)
