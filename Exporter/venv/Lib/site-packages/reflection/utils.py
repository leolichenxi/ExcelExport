try:
    import tkinter as tk
except ImportError:
    # Python 2
    import Tkinter as tk
import re

from . import constants
try:
    from .constants import PhotoImage
except ImportError:
    pass
try:
    from .constants import requests
except ImportError:
    from .constants import urlopen

__all__ = []


def validate_align(x):
    if not isinstance(x, str):
        raise TypeError(constants.ALIGN_NOT_STRING)
    if x not in constants.ALIGNMENTS:
        raise ValueError(constants.ALIGN_UNKNOWN)


def validate_anchor(x):
    if not isinstance(x, str):
        raise TypeError(constants.ANCHOR_NOT_STR)

    anchor_map = {"left": False, "right": False, "top": False, "bottom": False}
    for anchor in x.split("-"):
        if anchor not in constants.ANCHORS:
            raise ValueError(constants.ANCHOR_UNKNOWN)
        if anchor == "fill" and len(x.split("-")) > 1:
            raise ValueError(constants.ANCHOR_FILL_COMBINED)
        elif anchor == "left":
            if anchor_map["left"]:
                raise ValueError(constants.ANCHOR_REPEATED.format("'left'"))
            if anchor_map["right"]:
                raise ValueError(constants.ANCHOR_CONFLICT.format(
                    "'left'", "'right'")
                )
            anchor_map["left"] = True
        elif anchor == "right":
            if anchor_map["right"]:
                raise ValueError(constants.ANCHOR_REPEATED.format("'right'"))
            if anchor_map["left"]:
                raise ValueError(constants.ANCHOR_CONFLICT.format(
                    "'right'", "'left'")
                )
            anchor_map["right"] = True
        elif anchor == "top":
            if anchor_map["top"]:
                raise ValueError(constants.ANCHOR_REPEATED.format("'top'"))
            if anchor_map["bottom"]:
                raise ValueError(constants.ANCHOR_CONFLICT.format(
                    "'top'", "'bottom'")
                )
            anchor_map["top"] = True
        elif anchor == "bottom":
            if anchor_map["bottom"]:
                raise ValueError(constants.ANCHOR_REPEATED.format("'bottom'"))
            if anchor_map["top"]:
                raise ValueError(constants.ANCHOR_CONFLICT.format(
                    "'bottom'", "'top'")
                )
            anchor_map["bottom"] = True


def validate_color(x):
    if not isinstance(x, str):
        raise TypeError(constants.COLOR_NOT_STRING)
    if x not in constants.COLORS and not re.match(
        constants.HEX_COLOR, x.lower()
    ):
        raise ValueError(constants.COLOR_UNKNOWN)


def validate_column(x):
    validate_at_least("column", x=x, limit=0)


def validate_columnspan(x):
    validate_at_least("columnspan", x=x, limit=1)


def validate_expandcolumn(x):
    validate_at_least("expandcolumn", x=x, limit=0)


def validate_expandrow(x):
    validate_at_least("expandrow", x=x, limit=0)


def validate_height(x):
    validate_at_least("height", x=x, limit=1)


def validate_image(x):
    if not isinstance(x, str):
        raise TypeError(constants.IMAGE_NOT_STRING)
    if not os.path.isfile(x):
        raise FileNotFoundError(constants.IMAGE_NOT_FILE)


def validate_at_least(name, x, limit):
    if not isinstance(x, int):
        raise TypeError(constants.GENERIC_NOT_INTEGER.format(name))
    if x < limit:
        raise ValueError(constants.GENERIC_TOO_LOW.format(name, limit))


def validate_parent(x, widget, window):
    try:
        x.widget
        if not isinstance(x, (widget, window)):
            raise TypeError(constants.PARENT_WRONG_TYPE)
        return
    except AttributeError:
        exception = TypeError(constants.PARENT_WRONG_TYPE)
        exception.__cause__ = None
        raise exception


def validate_row(x):
    validate_at_least("row", x=x, limit=0)


def validate_rowspan(x):
    validate_at_least("rowspan", x=x, limit=1)


def validate_style(x):
    if not isinstance(x, styles.Style):
        raise TypeError(constants.STYLE_WRONG_TYPE)


def validate_title(x):
    if not isinstance(x, str):
        raise TypeError(constants.TITLE_NOT_STRING)


def validate_value(x):
    if not isinstance(x, str):
        raise TypeError(constants.VALUE_NOT_STRING)


def validate_width(x):
    validate_at_least("width", x=x, limit=1)


def validate_x_y_restrict(x, y):
    if y is not None:
        validate_height(y)
    if x is not None:
        validate_width(x)


def apply_style_recursively(instance, style):
    for widget in instance.widget.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.configure(**style.entrystyle.active)
        elif isinstance(widget, tk.Label):
            widget.configure(**style.textstyle.active)
        elif isinstance(widget, tk.Button):
            widget.configure(**style.buttonstyle.active)
        elif isinstance(widget, tk.Frame):
            widget.configure(**style.framestyle.active)


def load_photo_image(**kwargs):
    if constants.PIL_AVAILABLE:
        try:
            return PhotoImage(**kwargs)
        except OSError:
            pass
    try:
        return tk.PhotoImage(**kwargs)
    except tk.TclError:
        exception = ValueError(constants.IMAGE_BUFFER_FAILED)
        exception.__cause__ = None
        raise exception


def stream_image(url):
    image_bytes = []
    if constants.REQUESTS_AVAILABLE:
        try:
            request = requests.get(url, stream=True)
        except requests.exceptions.RequestException:
            pass
        else:
            for chunk in request.iter_content(constants.BUFFER_SIZE):
                image_bytes.append(chunk)
            image_bytes = bytes().join(image_bytes)
            return image_bytes
    try:
        file_descriptor = urlopen(url)
        buffered_reader = io.BufferedReader(file_descriptor)
        while True:
            chunk = buffered_reader.read(constants.BUFFER_SIZE)
            if not chunk:
                break
            image_bytes.append(chunk)
        image_bytes = bytes().join(image_bytes)
        return image_bytes
    except OSError:
        raise ConnectionError(constants.IMAGE_STREAM_FAILED)


def validate_and_standardize(**kwargs):
    for function, key in {
        (validate_height, "height"),
        (validate_align, "justify"),
        (validate_value, "text"),
        (validate_width, "width"),
    }:
        try:
            function(kwargs[key])
        except KeyError:
            pass
    try:
        foreground = kwargs["foreground"]
        validate_color(foreground)
        kwargs["foreground"] = constants.COLORS.get(foreground, foreground)
    except KeyError:
        pass
    try:
        background = kwargs["background"]
        validate_color(background)
        kwargs["background"] = constants.COLORS.get(background, background)
    except KeyError:
        pass
    return kwargs

for function in (
    apply_style_recursively,
    load_photo_image,
    stream_image,
    validate_align,
    validate_anchor,
    validate_color,
    validate_column,
    validate_columnspan,
    validate_expandcolumn,
    validate_expandrow,
    validate_height,
    validate_image,
    validate_parent,
    validate_row,
    validate_rowspan,
    validate_style,
    validate_title,
    validate_value,
    validate_width,
    validate_x_y_restrict,
):
    function.__doc__ = """Internal function."""
