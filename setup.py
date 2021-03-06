import io
from setuptools import setup, find_packages

main_ns = {}
exec(open("easy_dash/version.py").read(), main_ns)  # pylint: disable=exec-used


def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if l]
    return requires


INSTALL_REQUIRES = parse_requirements_file("requirements.txt")

setup(
    name="easy_dash",
    version=main_ns["__version__"],
    author="Kevin Mader",
    author_email="kevinmader@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    license="Apache",
    description=("Easy wrapper to make Dash apps easier"),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=INSTALL_REQUIRES,
    url="https://github.com/kmader/easy_dash",
    classifiers=[
        "Development Status :: 1 - Alpha/Unstable",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database :: Front-Ends",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Widget Sets",
    ],
)
