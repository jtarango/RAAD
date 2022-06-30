#!/usr/bin/python3
# -*- coding: utf-8 -*-
# *****************************************************************************/
# * Authors: Joseph Tarango
# *****************************************************************************/
import os, sys
importPathSuper = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.insert(1, importPathSuper)
importPath = os.path.abspath(os.getcwd())
sys.path.insert(1, importPath)

"""
Package system
"""
# Folders
from . import software

# Files
# from . import config
# from . import main
# from . import setup