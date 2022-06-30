# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os, sys, fnmatch, pprint

rootPathDir = os.path.abspath('../../')

excludesList = [".", "_", "__", "*external*", "__pycache__", "__init__.py", '*__.py']
includesList = ['*.py']

# Hack for bug on include paths
sys.path.append(os.path.abspath("../../src/software/autoAI"))
sys.path.append(os.path.abspath("../../src/software/TSV"))

sys.path.append(rootPathDir)
for _root, _dirs, _files in os.walk(rootPathDir):
    for _dir in _dirs:
        filepath = _root + os.sep + _dir
        absPathVar = os.path.abspath(os.path.join(_root, _dir))
        sys.path.append(absPathVar)

"""
import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

excludesList = [".", "_", "__", "*external*", "__pycache__"] # '*__.py' "__init__.py",
includesList = ['*.py']
excludeDir =['.git', 'git', '.idea', 'idea', '__pycache__', '_dev_tools', '.raadProfile', 'raadProfile', 'html']
rootPathDir = list()
rootFiles = list()

rootPathDir.append(os.path.abspath('../../src'))
rootPathDir.append(os.path.abspath('images'))
rootPathDir.append(os.path.abspath('.'))
rootPathDir.append(os.path.abspath('..'))

for _root, _dirs, _files in os.walk(os.path.abspath('../../src')):
    for _dir in _dirs:
        dpath_list = _dir.split(os.sep)
        rpath_list = _root.split(os.sep)
        isInIntersectionD = (len(set(dpath_list) & set(excludeDir)) > 0)
        isInIntersectionR = (len(set(rpath_list) & set(excludeDir)) > 0)
        if _dir in excludeDir or isInIntersectionD or isInIntersectionR:
            break
        else:
            filepath = _root + os.sep + _dir
            absPathVar = os.path.abspath(os.path.join(_root, _dir))
            rootPathDir.append(absPathVar)
            # sys.path.append(absPathVar)
    for _file in _files:
        if _file[-3:] in '.py':
            rootFiles.append(_root)
            # sys.path.append(_root)
            break
"""
print("Root Path Directory")
pprint.pprint(rootPathDir)

def _filter(paths):
    matches = []

    for path in paths:
        append = None

        for include in includesList:
            if os.path.isdir(path):
                append = True
                break

            if fnmatch.fnmatch(path, include):
                append = True
                break

        for exclude in excludesList:
            if os.path.isdir(path) and path == exclude:
                append = False
                break

            if fnmatch.fnmatch(path, exclude):
                append = False
                break

        if append:
            matches.append(path)

    return matches
    
def addAll():
    thisDir = rootPathDir # os.path.abspath('../../')

    print("Root Search Path Directory")
    pprint.pprint(thisDir)

    sourceList = []
    if isinstance(thisDir, list):
        for selectPath in thisDir:
            for root, dirs, files in os.walk(selectPath):
                dirs[:] = _filter(map(lambda d: os.path.join(root, d), dirs))
                files[:] = _filter(map(lambda f: os.path.join(root, f), files))

                for filename in files:
                    filename = os.path.join(root, filename)
                    print("Added Path Directory {}".format(filename))
                    sourceList.append(filename)
    else:
        for root, dirs, files in os.walk(thisDir):
            dirs[:] = _filter(map(lambda d: os.path.join(root, d), dirs))
            files[:] = _filter(map(lambda f: os.path.join(root, f), files))

            for filename in files:
                filename = os.path.join(root, filename)
                print("Added Path Directory {}".format(filename))
                sourceList.append(filename)
    for sourceFile in sourceList:
        sys.path.insert(0, os.path.abspath(sourceFile))


# -- Project information -----------------------------------------------------

project = 'RAAD'
copyright = '2022, Joseph Tarango'
author = 'Joseph Tarango'

version = '1.0.0'

release = 'Alpha'

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
]

set_type_checking_flag = True

napoleon_google_docstring = False

templates_path = ['_templates']

source_suffix = ['.rst', '.md']

master_doc = 'index'

exclude_patterns = []

todo_include_todos = True

html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
html_static_path = []
