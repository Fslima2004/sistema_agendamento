from setuptools import setup, find_packages

setup(
    name="sistema_agendamento",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": ["flake8", "mypy", "pytest"]
    },
    python_requires=">=3.8",
)
