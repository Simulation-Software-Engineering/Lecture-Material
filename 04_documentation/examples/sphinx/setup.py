import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jaustar-SSE-package",
    version="0.0.1",
    author="Alexander Jaust",
    author_email="alexander.jaust@ipvs.uni-stuttgart.de",
    description="A small description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simulation-Software-Engineering/test-exercise-packaging",
    project_urls={
        "Bug Tracker": "https://github.com/Simulation-Software-Engineering/test-exercise-packaging/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
