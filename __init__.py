"""
Entry point for Sentence Miner add-on from Anki.

Performs any migration tasks and then loads the 'sentminer' package.
"""

from sys import stderr

from . import sentminer

if __name__ == '__main__':
    stderr.write(
        'sentminer is a sentence miner add-on for Anki.\n'
        'To learn more or download Anki, visit <https://apps.ankiweb.net>.\n'
    )
    exit(1)
