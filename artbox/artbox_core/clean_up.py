import os

"""Cleans up the image files when deleted or edited from the db"""


def clean_up(path):
    if path:
        os.remove(path)
