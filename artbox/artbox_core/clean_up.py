import os


def clean_up(path):
    if path:
        os.remove(path)
