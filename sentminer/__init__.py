"""
Add-on package initialization.
"""

import aqt

__all__ = ['editor_button']

def editor_button():
    """
    Enable the sentence mining through the editor,
    which is present in the "Add" and browser windows.
    """

    

    # def createAwesomeTTSEditorLambda():
    #     def launch(editor):
    #         editor_generator = gui.EditorGenerator(editor=editor,
    #                                                addon=addon,
    #                                                alerts=aqt.utils.showWarning,
    #                                                ask=aqt.utils.getText,
    #                                                parent=editor.parentWindow)
    #         editor_generator.show()
    #     return launch

    # def addAwesomeTTSEditorButton(buttons, editor):
    #     new_button = editor.addButton(gui.ICON_FILE,
    #         'AwesomeTTS',
    #         createAwesomeTTSEditorLambda(),
    #         tip = "Record and insert an audio clip here w/ AwesomeTTS")
    #     buttons.append(new_button)
    #     return buttons

    # aqt.gui_hooks.editor_did_init_buttons.append(addAwesomeTTSEditorButton)

    # def createAwesomeTTSEditorShortcutLambda(editor):
    #     def launch():
    #         editor_generator = gui.EditorGenerator(editor=editor,
    #                                                addon=addon,
    #                                                alerts=aqt.utils.showWarning,
    #                                                ask=aqt.utils.getText,
    #                                                parent=editor.parentWindow)
    #         editor_generator.show()
    #     return launch

    # def editor_init_shortcuts(shortcuts, editor: aqt.editor.Editor):
    #     shortcut_sequence = sequences['editor_generator'].toString()
    #     lambda_function = createAwesomeTTSEditorShortcutLambda(editor)
    #     shortcut_entry = (shortcut_sequence, lambda_function, True)
    #     shortcuts.append(shortcut_entry)

    # aqt.gui_hooks.editor_did_init_shortcuts.append(editor_init_shortcuts)