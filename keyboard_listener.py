

import pyHook
import pythoncom
from transform_image_to_text import main


def OnKeyBoardEvent(event):
    # if event.KeyID <65 or event.KeyID >122:
        # return False

    if event.Key != 'F1':
        return False

    main()
    return True


hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyBoardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
