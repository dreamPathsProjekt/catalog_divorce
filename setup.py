from setuptools import setup, find_packages

setup(
    name="catalog_divorce",
    version="0.1",
    packages=find_packages(),


    # install_requires=['docutils>=0.3'],

    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['*.txt', '*.rst'],
    #     # And include any *.msg files found in the 'hello' package, too:
    #     'hello': ['*.msg'],
    # },

    # metadata for upload to PyPI
    author="Dream Paths Projekt",
    author_email="dream.paths.projekt@gmail.com",
    description="A command line tool to easily find duplicates between different folder structures",
    license="MIT",
    keywords="duplicates python folders cmd",
    # url="http://example.com/HelloWorld/",
)
