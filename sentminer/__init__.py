"""
Add-on package initialization.
"""

from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo, qconnect
from anki.hooks import addHook

from .paths import ICONS

# cross out the currently selected text
def on_strike(editor):
    editor.web.eval("wrap('<b>', '</b>');")

def test_function() -> None:
    cardCount = mw.col.cardCount()
    showInfo("Card count: %d" % cardCount)

def add_sentminer_button(buttons, editor):
    editor._links['strike'] = test_function
    return buttons + [editor._addButton(
        f"{ICONS}/sentminer_logo_crop.ico",
        "strike",
        "Mining sentence in English and insert here with Sentminer")]

addHook("setupEditorButtons", add_sentminer_button)