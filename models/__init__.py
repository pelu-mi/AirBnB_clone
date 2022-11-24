#!/usr/bin/python3
"""
Project initialization file
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
