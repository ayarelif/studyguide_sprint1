# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="studyguide_sprint1", # the name that you will install via pip
    version="0.0.1",
    author="Elif Ayar",
    author_email="your@email.com",
    description="extra practice files for the sprint 1",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ayarelif/studyguide_sprint1",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)