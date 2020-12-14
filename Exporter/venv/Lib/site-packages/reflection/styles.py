try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from . import constants

__all__ = [
    "Style",
]


class StyleObject(object):
    def __init__(self, options):
        self.options = options
        self.active = {}

    def configure(self, **options):
        for key in options:
            if key not in self.options:
                raise ValueError(constants.STYLE_OPTION_UNKNOWN.format(
                    str(list(self.options.keys()))[1:-1])
                )
            self.active[key] = options[key]


class Style(object):
    def __init__(self):
        self.buttonstyle = StyleObject(constants.BUTTON_OPTIONS)
        self.windowstyle = StyleObject(constants.WINDOW_OPTIONS)
        self.framestyle = StyleObject(constants.FRAME_OPTIONS)
        self.entrystyle = StyleObject(constants.ENTRY_OPTIONS)
        self.textstyle = StyleObject(constants.TEXT_OPTIONS)
