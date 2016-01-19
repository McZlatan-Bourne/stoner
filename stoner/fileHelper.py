#!/usr/bin/env python

import os

def checkfile(path):
				"""Confirms file to be uploaded."""
				if os.path.isfile(path) == True and os.path.exists(path) == True:
								return str(path)
				else:return False
