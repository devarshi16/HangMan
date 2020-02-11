import setuptools
from setuptools import find_packages
import os

def find_data(relpath, folder):
    dir_content = []
    path = os.path.join(relpath, folder)
    tree = [(dirname, filenames) for dirname, _, filenames in os.walk(path)
            if filenames]

    for root, files in tree:
        path = os.path.relpath(root, relpath)
        dir_content.extend(map(lambda x: os.path.join(path, x), files))

    return dir_content


def package_data(relpath, folders):
    all_files = []
    for folder in folders:
        all_files.extend(find_data(relpath, folder))

    return all_files

with open("README.md", "r") as fh:
    long_description = """
    A Game of Hangman
    Save the Man by guessing the word correctly
    Available wordlists are Animals, Pokemons,
    Fruits, Countries, Bollywood Movies.
    """
setuptools.setup(
     name='hangman-ultimate',  
     version='1.0.2',
     author="devarshi16",
     author_email="devershigpt6@gmail.com",
     description="A Game of Hangman",
     long_description=long_description,
     url="https://github.com/devarshi16/HangMan",
     packages=find_packages(),
     keywords="hangman hangman-game python-tutorial hangman-python terminal-game game pokemon",
     package_data={
         "hangmanultimate":package_data("hangmanultimate",["data"]),
     },
     #include_package_data=True,
     classifiers=[
         "Development Status :: 4 - Beta",
         "Programming Language :: Python :: 3.5",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Unix",
     ],
     entry_points = {
         "console_scripts": ['hangman-ultimate = hangmanultimate.hangman:main']
     },
     python_requires=">=3.5",
     install_requires=[
        'readchar>=2.0.1',
        'termcolor>=1.1.0'
     ],
 )
