import setuptools
import os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_requirements():
    """parses requirements from requirements.txt"""
    reqs_path = os.path.join(__location__, "requirements.txt")
    with open(reqs_path, encoding="utf8") as f:
        reqs = [line.strip() for line in f if not line.strip().startswith("#")]

    names = []
    links = []
    for req in reqs:
        if "://" in req:
            links.append(req)
        else:
            names.append(req)
    return {"install_requires": names, "dependency_links": links}


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rus_rule_based_insult_classifier-kudep",
    version="v0.8.1",
    author="Kuznensov Denis",
    author_email="kuznetsov.den.p@gmail.com",
    keywords=["Russian Language", "rule-based insult classifier", "NLP"],
    description="Rule-based insult classifier for the Russian language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kudep/rus_rule_based_insult_classifier",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    **read_requirements()
)
