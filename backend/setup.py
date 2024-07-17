from setuptools import setup, find_packages

setup(
    name="fastapp",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi==0.111.1", # cross-check with requirements.txt
        "uvicorn==0.30.1", # ditto
    ],
    # entry_points={
    #     "console_scripts": [
    #         "run-fastapp=fastapp.main:run",
    #     ],
    # },
)