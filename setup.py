import setuptools

# we need to read our readme file because this is required during pypi package publishing as package desciption
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarisation-NLP"
AUTHOR_USER_NAME = "JainilRana"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "jainil133.rana@gmail.com"


# this will loook for constructor file in every folder and install it wherever required
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)