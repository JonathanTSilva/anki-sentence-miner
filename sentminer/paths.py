"""
Path and directory initialization
"""

import os
import tempfile

__all__ = [
    'ADDON',
    'ADDON_IS_LINKED',
    'CACHE',
    'CONFIG',
    'LOG',
    'TEMP',
    'ICONS'
]

ADDON = os.path.dirname(os.path.abspath(__file__))

ADDON_IS_LINKED = os.path.islink(ADDON)

BLANK = os.path.join(ADDON, 'blank.mp3')

ICONS = os.path.join(ADDON, 'gui/icons')

ROOT = os.path.dirname(ADDON)

USER_FILES = os.path.join(ROOT, 'user_files')

# mp3 file cache
CACHE = os.path.join(USER_FILES, 'cache')
os.makedirs(CACHE, exist_ok=True)

CONFIG = os.path.join(USER_FILES, 'config.db')

LOG = os.path.join(ADDON, 'addon.log')

TEMP = tempfile.gettempdir()
