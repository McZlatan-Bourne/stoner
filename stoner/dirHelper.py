#!/usr/bin/env python

import os

def getCurrentDirectory():
    """Returns the current working directory"""
    cwd = os.getcwd()
    return str(cwd)
