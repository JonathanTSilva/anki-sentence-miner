"""
Add-on package initialization.
"""

from aqt.utils import showInfo
from anki.hooks import addHook

from .paths import ICONS

# cross out the currently selected text
def on_strike(editor):
    editor.web.eval("wrap('<del>', '</del>');")

def add_my_button(buttons, editor):
    editor._links['strike'] = on_strike
    return buttons + [editor._addButton(
        f"{ICONS}/sentminer_logo_crop.ico",
        "strike",
        "Mining sentence in English and insert here with Sentminer")]

addHook("setupEditorButtons", add_my_button)
