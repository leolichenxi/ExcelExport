import abc
import io
import os
import re
try:
    import tkinter as tk
except ImportError:
    # Python 2.
    import Tkinter as tk

from . import constants
from . import styles
from .exceptions import (
    TkinterException,
)
from .utils import (
    apply_style_recursively,
    load_photo_image,
    validate_align,
    validate_anchor,
    validate_and_standardize,
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
)

__all__ = [
    "Application",
    "Button",
    "Entry",
    "Frame",
    "Image",
    "Text",
    "TkinterException",
    "Window",
]

global tk_
tk_ = None
global hierarchy
hierarchy = {}


def require_tk(name, instance):
    """Internal function."""
    global tk_
    if not tk_:
        raise ValueError(constants.APPLICATION_NOT_EXISTS.format(name))
    elif not instance.widget.winfo_exists():
        # The widget doesn't exist (has been destroyed).
        raise ValueError(constants.WIDGET_DESTROYED.format(name))


class Application(object):
    """Represents the control point for an interface.

    When instantiating the object, an associated Tcl interpreter is
    started through the underlying ``Tk`` widget. Only one
    ``Application`` instance may exist at a given time.

    :method __init__: Constructor.
    :method destroy: Destroy the application and its associated widgets.
    :method run: Run the event loop.
    """
    def __init__(self):
        """Constructor.

        :raises ValueError: If an ``Application`` instance already
                            exists.
        :return: None.
        :rtype: ``None``
        """
        global tk_
        if tk_:
            # A Tk object already exists.
            raise ValueError(constants.APPLICATION_ALREADY_EXISTS)
        tk_ = self
        self.widget = tk.Tk()
        self.widget.wm_withdraw()

    def destroy(self):
        """Destroy the application and its associated widgets.

        Note that after destroying the ``Application`` instance, all
        associated widgets will be destroyed and can't be used anymore.

        :raises ValueError: If the instance has already been destroyed.
        :return: None.
        :rtype: ``None``
        """
        global tk_
        if not tk_:
            # No Tk object remains, so the widget must already
            # have been destroyed.
            raise ValueError(constants.OBJECT_ALREADY_DESTROYED)
        else:
            # Only this Tk object remains.
            tk_ = None
            self.widget.destroy()

    def run(self):
        """Run the event loop.

        :return: None.
        :rtype: ``None``
        """
        require_tk("run", self)
        self.widget.mainloop()


class Widget(object):
    """Represents a visual element.

    :method __init__: Constructor.
    :method destroy: Destroy the widget and its children.
    :method disable: Deactivate the widget.
    :method display: Display the widget.
    :method enable: Activate the widget.
    :method focus: Delegate focus to the widget.
    :method get_style: Get the widget's style.
    :method hide: Hide the widget.
    :method set_style: Set the widget's style.
    :property children: Get the widget's children.
    :property parent: Get the widget's parent.
    """
    def __init__(self, parent, wtype, **kwargs):
        """Constructor.

        :param parent: A valid parent for the widget
                       (a ``Widget`` or ``Window`` instance).
        :param wtype: The Tcl widget to be instantiated.
        :param \*\*kwargs: The keyword arguments to be passed to
                           ``wtype``.
        :return: None.
        :rtype: ``None``
        """
        global tk_
        if not tk_:
            raise ValueError(constants.OBJECT_CANT_CREATE)

        validate_parent(parent, Widget, Window)

        kwargs = validate_and_standardize(**kwargs)
        try:
            image = kwargs["image"]
            image_path = kwargs["image_path"]
            kwargs.pop("image_path")
        except KeyError:
            pass
        self.widget = wtype(master=parent.widget, **kwargs)
        try:
            self.widget.__image_cache = image
            self.widget.__image_path = image_path
        except NameError:
            pass

        global hierarchy
        hierarchy[self] = []
        # Children of the widget to be contained within this list.
        hierarchy[parent].append(self)
        self.style = styles.Style()

        try:
            self.set_value(kwargs["text"])
        except (NameError, AttributeError):
            pass

    def destroy(self):
        """Destroy the widget and its children.

        :return: None.
        :rtype: ``None``
        """
        require_tk("destroy", self)
        self.hide()
        self.widget.destroy()

    def disable(self):
        """Deactivate the widget.

        Some widget may not show any response to this action. If the
        widget is already disabled, this will not have any effect.

        :raises ValueError: If the underlying widget does not support
                            switching state.
        :return: None.
        :rtype: ``None``
        """
        require_tk("disable", self)
        try:
            self.widget.configure(state="disabled")
            return
        except tk.TclError:
            # The widget does not support switching state.
            exception = ValueError(constants.WIDGET_CANT_SET_STATE)
            exception.__cause__ = None
            raise exception

    def display(
                self,
                row,
                column,
                rowspan=1,
                columnspan=1,
                expandrow=0,
                expandcolumn=0,
                anchor="fill"
               ):
        """Display the widget.

        :param int row: The row to contain the widget. Must be at least
                        0. If ``None`` is passed instead, use the cached
                        row value.
        :param int column: The column to contain the widget. Must be at
                           least 0. If ``None`` is passed instead, use
                           the cached column value.
        :param int rowspan: The amount of rows to span the widget
                            across. Must be at least 1. Defaults to 1.
        :param int columnspan: The amount of columns to span the widget
                               across. Must be at least 1. Defaults to
                               1.
        :param int expandrow: The speed at which to expand the widget
                              within the row, when the parent resizes.
                              Set to 0 to disable expanding. Must be at
                              least 0. Defaults to 0.
        :param int expandcolumn: The speed at which to expand the widget
                                 within the column, when the parent
                                 resizes. Set to 0 to disable expanding.
                                 Must be at least 0. Defaults to 0.
        :param str anchor: Way to place the widget within its parent if
                           it doesn't fill the space allotted by its
                           parent. Must be any of 'left', 'right',
                           'bottom', 'top', 'fill'. Anchor arguments can
                           be combined by separating them with a dash:
                           A valid specification could be 'bottom-left',
                           or 'top-right'. 'fill' cannot be used in
                           combination with other arguments.
                           Defaults to 'fill'.
        :raises TypeError: If ``row`` is not an integer.
        :raises TypeError: If ``column`` is not an integer.
        :raises TypeError: If ``rowspan`` is not an integer.
        :raises TypeError: If ``expandrow`` is not an integer.
        :raises TypeError: If ``expandcolumn`` is not an integer.
        :raises TypeError: If ``anchor`` is not a string.
        :raises ValueError: If ``row`` is less than 0.
        :raises ValueError: If ``column`` is less than 0.
        :raises ValueError: If ``rowspan`` is less than 1.
        :raises ValueError: If ``columnspan`` is less than 1.
        :raises ValueError: If ``expandrow`` is less than 0.
        :raises ValueError: If ``expandcolumn`` is less than 0.
        :raises ValueError: If ``anchor`` is not any of 'left', 'right',
                            'bottom', 'top', 'fill', or a combination.
        :raises ValueError: If ``anchor`` is a combination of arguments
                            and any of these arguments is not any of
                            'left', 'right', 'top', 'bottom', 'fill'.
        :raises ValueError: If ``anchor`` is a combination of arguments
                            and any of these arguments is 'fill'.
        :raises ValueError: If ``anchor`` is a combination of arguments
                            and an argument is repeated.
        :raises ValueError: If ``anchor`` is a combination of arguments
                            and conflicting arguments are given
                            ('left' and 'right' or 'top' and 'bottom').
        :return: None.
        :rtype: ``None``
        """
        require_tk("display", self)
        validate_row(row)
        validate_column(column)
        validate_rowspan(rowspan)
        validate_columnspan(columnspan)
        validate_expandrow(expandrow)
        validate_expandcolumn(expandcolumn)
        validate_anchor(anchor)
        anchor = "".join([constants.ANCHORS[n] for n in anchor.split("-")])

        self.widget.master.grid_rowconfigure(row, weight=expandrow)
        self.widget.master.grid_columnconfigure(column, weight=expandcolumn)
        self.widget.grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=anchor
        )

    def enable(self):
        """Activate the widget.

        Some widgets may not show any response to this action. If the
        widget is already enabled, this will not have any effect.

        :raises ValueError: If the underlying widget does not support
                            switching state.
        :return: None.
        :rtype: ``None``
        """
        require_tk("enable", self)
        try:
            self.widget.configure(state="normal")
            return
        except tk.TclError:
            # The widget does not support switching state.
            exception = ValueError(constants.WIDGET_CANT_SET_STATE)
            exception.__cause__ = None
            raise exception

    def focus(self):
        """Delegate focus to the widget.

        If the widget already has focus, this has no effect.

        :return: None.
        :rtype: ``None``
        """
        require_tk("focus", self)
        self.widget.focus_set()

    def get_style(self):
        """Get the widget's style.

        :return: The widget's style.
        :rtype: ``styles.Style``
        """
        require_tk("get_style", self)
        return self.style

    def hide(self):
        """Hide the widget.

        If the widget is already hidden, this has no effect.

        :return: None.
        :rtype: ``None``
        """
        require_tk("hide", self)
        self.widget.grid_forget()

    def set_style(self, style, recursive=False):
        """Set the widget's style.

        :param style: A ``styles.Style`` object.
        :param bool recursive: Apply the style not just to this widget,
                               but also to all of its children. Defaults
                               to ``False``.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_style", self)
        validate_style(style)
        stylename = self.__class__.__name__.lower() + "style"
        self.widget.configure(**getattr(style, stylename).active)
        self.style = style
        if recursive:
            apply_style_recursively(self, style=style)

    @property
    def children(self):
        """Get the widget's children.

        :return: A list of the widget's children.
        :rtype: ``list<Widget>``
        """
        return hierarchy[self]

    @property
    def parent(self):
        """Get the widget's parent.

        :return: The widget's parent.
        :rtype: ``Widget`` or ``Window`` instance.
        """
        for widget in hierarchy:
            if self in hierarchy[widget]:
                return widget


class TextWidget(Widget):
    """Represents a widget capable of displaying text.

    :method __init__: Constructor.
    :method get_align: Get the text's alignment.
    :method get_background: Get the backgroundcolor.
    :method get_foreground: Get the textcolor.
    :method get_value: Get the text value.
    :method set_align: Set the text's alignment.
    :method set_background: Set the backgroundcolor.
    :method set_foreground: Set the textcolor.
    :method set_value: Set the text value.

    Superclass Widget
    =================
    Represents a visual element.

    :method __init__: Constructor.
    :method destroy: Destroy the widget and its children.
    :method disable: Deactivate the widget.
    :method display: Display the widget.
    :method enable: Activate the widget.
    :method focus: Delegate focus to the widget.
    :method get_style: Get the widget's style.
    :method hide: Hide the widget.
    :method set_style: Set the widget's style.
    :property children: Get the widget's children.
    :property parent: Get the widget's parent.
    """
    def __init__(
                 self,
                 parent,
                 wtype,
                 value,
                 foreground,
                 background,
                 align,
                 **kwargs
                ):
        """Constructor.

        :param parent: A valid parent for the widget
                       (a ``Widget`` or ``Window`` instance).
        :param wtype: The Tcl widget to be instantiated.
        :param str value: The initial text value.
        :param str foreground: The textcolor. Must be any of 'white',
                               'black', 'red', 'green', 'blue',
                               'yellow', 'orange', 'grey', 'gray',
                               'pink', 'purple', or be a valid hex color
                               code.
        :param str background: The background color. Must be any of
                               'white', 'black', 'red', 'green', 'blue',
                               'yellow', 'orange', 'grey', 'gray',
                               'pink', 'purple', or be a valid hex color
                               code.
        :param str align: The text's alignment. Must be any of 'left',
                          'right', 'center'.
        :param \*\*kwargs: Other keyword arguments to be passed to
                           ``wtype``.
        :return: None.
        :rtype: ``None``
        """
        super(TextWidget, self).__init__(
            parent=parent,
            wtype=wtype,
            text=value,
            foreground=foreground,
            background=background,
            justify=align,
            **kwargs
        )

    def get_align(self):
        """Get the text's alignment.

        :return: The alignment specification. Always any of 'left',
                 'right', 'center'.
        :rtype: ``str``
        """
        require_tk("get_align", self)
        return self.widget.cget("justify")

    def get_background(self):
        """Get the backgroundcolor.

        :return: The backgroundcolor as a hex color code.
        :rtype: ``str``
        """
        require_tk("get_background", self)
        return self.widget.cget("background")

    def get_foreground(self):
        """Get the textcolor.

        :return: The textcolor as a hex color code.
        :rtype: ``str``
        """
        require_tk("get_foreground", self)
        return self.widget.cget("foreground")

    def get_value(self):
        """Get the text value.

        :return: The text value.
        :rtype: ``str``
        """
        require_tk("get_value", self)
        return self.widget.cget("text")

    def set_align(self, align):
        """Set the text's alignment.

        :param str align: The alignment specification. Must be any of
                          'left', 'right', 'center'.
        :raises TypeError: If ``align`` is not a string.
        :raises ValueError: If ``align`` is not any of 'left', 'right',
                            'center'.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_align", self)
        validate_align(align)
        self.widget.configure(justify=align)

    def set_background(self, background):
        """Set the backgroundcolor.

        :param str background: The backgroundcolor. Must be any of
                               'white', 'black', 'red', 'green', 'blue',
                               'yellow', 'orange', 'grey', 'gray',
                               'pink', 'purple', or be a valid hex color
                               code.
        :raises TypeError: If ``background`` is not a string.
        :raises ValueError: If ``background`` is not a named color or a
                            valid hex color code.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_background", self)
        validate_color(background)
        self.widget.configure(
            background=constants.COLORS.get(background, background)
        )

    def set_foreground(self, foreground):
        """Set the textcolor.

        :param str foreground: The foreground color. Must be any of
                               'white', 'black', 'red', 'green', 'blue',
                               'yellow', 'orange', 'grey', 'gray',
                               'pink', 'purple', or be a valid hex color
                               code.
        :raises TypeError: If ``foreground`` is not a string.
        :raises ValueError: If ``foreground`` is not a named color or a
                            valid hex color code.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_foreground", self)
        validate_color(foreground)
        self.widget.configure(
            foreground=constants.COLORS.get(foreground, foreground)
        )

    def set_value(self, value):
        """Set the text value.

        :param str value: The text value.
        :raises TypeError: If ``value`` is not a string.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_value", self)
        self.widget.configure(text=value)


class Window(object):
    """Represents an application's 'Window'.

    A ``Window`` instance does not have a parent and therefore
    doesn't qualify as a widget. However, you can specify a ``Window``
    instance as a parent for widgets.

    :method __init__: Constructor.
    :method destroy: Destroy the window and its children.
    :method focus: Delegate focus to the window.
    :method get_background: Get the window's backgroundcolor.
    :method get_height: Get the window's height.
    :method get_maxsize: Get the window's maxsize specification.
    :method get_minsize: Get the window's minsize specification.
    :method get_style: Get the window's style.
    :method get_title: Get the window's title.
    :method get_width: Get the window's width.
    :method hide: Hide the window.
    :method set_background: Set the window's backgroundcolor.
    :method set_height: Set the window's height.
    :method set_maxsize: Set the window's maxsize specification.
    :method set_minsize: Set the window's minsize specification.
    :method set_style: Set the window's style.
    :method set_title: Set the window's title.
    :method set_width: Set the window's width.
    :method display: Display the window.
    :property children: Get the window's children.
    """
    def __init__(
                 self,
                 width=400,
                 height=400,
                 background="white",
                 title=""
                ):
        """Constructor.

        :param int width: The window's width in pixels. Must be at least
                          1. Defaults to 400. Note that Tcl may impose
                          its own minimum width.
        :param int height: The window's height in pixels. Must be at
                           least 1. Defaults to 400. Note that Tcl may
                           impose its own minimum height.
        :param str background: The window's backgroundcolor. Must be
                               any of 'white', 'black', 'red', 'green',
                               'blue', 'yellow', 'orange', 'grey',
                               'gray', 'pink', 'purple', or be a valid
                               hex color code. Defaults to 'white'.
        :param str title: The window's title. Defaults to ''.
        :raises TypeError: If ``width`` is not an integer.
        :raises TypeError: If ``height`` is not an integer.
        :raises TypeError: If ``background`` is not a string.
        :raises ValueError: If ``width`` is less than 1.
        :raises ValueError: If ``height`` is less than 1.
        :raises ValueError: If ``background`` is not a named color or a
                            valid hex color code.
        :return: None.
        :rtype: ``None``
        """
        if not tk_:
            raise ValueError(constants.OBJECT_CANT_CREATE)
        validate_width(width)
        validate_height(height)
        validate_title(title)
        validate_color(background)
        background = constants.COLORS.get(background, background)
        self.widget = tk.Toplevel(
            master=tk_.widget,
            width=width,
            height=height,
            background=background,
        )
        self.set_title(title=title)
        self.hide()

        global hierarchy
        hierarchy[self] = []
        self.style = None

    def destroy(self):
        """Destroy the window and its children.

        :return: None.
        :rtype: ``None``
        """
        require_tk("destroy", self)
        self.widget.wm_withdraw()
        self.widget.destroy()

    def focus(self):
        """Delegate focus to the window.

        If the window already has focus, this has no effect.

        :return: None.
        :rtype: ``None``
        """
        require_tk("focus", self)
        self.widget.focus_set()

    def get_background(self):
        """Get the windows's backgroundcolor.

        :return: The backgroundcolor as a hex color code.
        :rtype: ``str``
        """
        require_tk("get_background", self)
        return self.widget.cget("background")

    def get_height(self):
        """Get the window's height.

        :return: The window's height in pixels.
        :rtype: ``int``
        """
        require_tk("get_height", self)
        return self.widget.winfo_height()

    def get_maxsize(self):
        """Get the window's maxsize specification.

        :return: The maximum window size in pixels as a (width, height)
                 tuple.
        :rtype: ``tuple``
        """
        require_tk("get_maxsize", self)
        return self.widget.wm_maxsize()

    def get_minsize(self):
        """Get the window's minsize specification.

        :return: The minimum window size in pixels as a (width, height)
                 tuple.
        :rtype: ``tuple``
        """
        require_tk("get_minsize", self)
        return self.widget.wm_minsize()

    def get_style(self):
        """Get the window's style.

        :return: The window's style.
        :rtype: ``styles.Style``
        """
        require_tk("get_style", self)
        return self.style

    def get_title(self):
        """Get the window's title.

        :return: The window's title.
        :rtype: ``str``
        """
        require_tk("get_title", self)
        return self.widget.wm_title()

    def get_width(self):
        """Get the window's width.

        :return: The window's width in pixels.
        :rtype: ``int``
        """
        require_tk("get_width", self)
        return self.widget.winfo_width()

    def hide(self):
        """Hide the window.

        If the window is already hidden, this has no effect.

        :return: None.
        :rtype: ``None``
        """
        require_tk("hide", self)
        self.widget.wm_withdraw()

    def set_background(self, background):
        """Set the window's backgroundcolor.

        :param str background: The backgroundcolor. Must be any of
                               'white', 'black', 'red', 'green', 'blue',
                               'yellow', 'orange', 'grey', 'gray',
                               'pink', 'purple', or be a valid hex color
                               code.
        :raises TypeError: If ``background`` is not a string.
        :raises ValueError: If ``background`` is not a named color or a
                            valid hex color code.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_background", self)
        validate_color(background)
        self.widget.configure(
            background=constants.COLORS.get(background, background)
        )

    def set_height(self, height):
        """Set the window's height.

        :param int height: The height in pixels. Must be at least 1.
                           Note that Tcl may impose its own minimum
                           height.
        :raises TypeError: If ``height`` is not an integer.
        :raises ValueError: If ``height`` is less than 1.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_height", self)
        validate_height(height)
        self.widget.configure(height=height)

    def set_maxsize(self, width=None, height=None):
        """Set the window's maxsize specification.

        :param int width: The maximum width in pixels. Must be at least
                          1. If ``None`` is passed instead, this
                          parameter is ignored. Defaults to ``None``.
        :param int height: The maximum height in pixels. Must be at
                           least 1. If ``None`` is passed instead, this
                           parameter is ignored. Defaults to ``None``.
        :raises TypeError: If ``width`` is not an integer or ``None``.
        :raises TypeError: If ``height`` is not an integer or ``None``.
        :raises ValueError: If ``width`` is less than 1.
        :raises ValueError: If ``height`` is less than 1.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_maxsize", self)
        validate_x_y_restrict(width, height)
        self.widget.wm_maxsize(height=height, width=width)

    def set_minsize(self, width=None, height=None):
        """Set the window's minsize specification.

        :param int width: The minimum width in pixels. Must be at least
                          1. If ``None`` is passed instead, this
                          parameter is ignored. Defaults to ``None``.
        :param int height: The minimum height in pixels. Must be at
                           least 1. If ``None`` is passed instead, this
                           parameter is ignored. Defaults to ``None``.
        :raises TypeError: If ``width`` is not an integer or ``None``.
        :raises TypeError: If ``height`` is not an integer or ``None``.
        :raises ValueError: If ``width`` is less than 1.
        :raises ValueError: If ``height`` is less than 1.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_minsize", self)
        validate_x_y_restrict(width, height)
        self.widget.wm_minsize(height=height, width=width)

    def set_style(self, style, recursive=False):
        """Set the window's style.

        :param style: A ``styles.Style`` object.
        :param bool recursive: Apply the style not just to this widget,
                               but also to all of its children. Defaults
                               to ``False``.
        :raises TypeError: If ``style`` is not a ``styles.Style``
                           object.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_style", self)
        validate_style(style)
        stylename = self.__class__.__name__.lower() + "style"
        self.widget.configure(**getattr(style, stylename).active)
        self.style = style
        if recursive:
            apply_style_recursively(self, style=style)

    def set_title(self, title):
        """Set the window's title.

        :param str title: The title.
        :raises TypeError: If ``title`` is not a string.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_title", self)
        validate_title(title)
        self.widget.wm_title(title)

    def set_width(self, width):
        """Set the window's width.

        :param int width: The width in pixels. Must be at least 1.
                          Note that Tcl may impose its own minimum
                          width.
        :raises TypeError: If ``width`` is not an integer.
        :raises ValueError: If ``width`` is less than 1.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_width", self)
        validate_width(width)
        self.widget.configure(width=width)

    def display(self):
        """Display the window.

        If the window is already visible, this has no effect.

        :return: None.
        :rtype: ``None``
        """
        require_tk("display", self)
        self.widget.deiconify()

    @property
    def children(self):
        """Get the window's children.

        :return: A list of the window's children.
        :rtype: list<Widget>
        """
        return hierarchy[self]


class Frame(Widget):
    """Represents a container for other widgets.

    :method __init__: Constructor.
    :method get_background: Get the frame's backgroundcolor.
    :method get_height: Get the frame's height.
    :method get_width: Get the frame's width.
    :method set_background: Set the frame's backgroundcolor.
    :method set_height: Set the frame's height.
    :method set_width: Set the frame's width.

    Superclass Widget
    =================
    Represents a visual element.

    :method __init__: Constructor.
    :method destroy: Destroy the widget and its children.
    :method disable: Deactivate the widget.
    :method display: Display the widget.
    :method enable: Activate the widget.
    :method focus: Delegate focus to the widget.
    :method get_style: Get the widget's style.
    :method hide: Hide the widget.
    :method set_style: Set the widget's style.
    :property children: Get the widget's children.
    :property parent: Get the widget's parent.
    """

    def __init__(
                 self,
                 parent,
                 width=200,
                 height=200,
                 background="white"
                ):
        super(Frame, self).__init__(
            parent=parent,
            wtype=tk.Frame,
            width=width,
            height=height,
            background=background
        )

    def get_background(self):
        """Get the frame's backgroundcolor.

        :return: The backgroundcolor as a hex color code.
        :rtype: ``str``
        """
        require_tk("get_background", self)
        return self.widget.cget("background")

    def get_height(self):
        """Get the frame's height.

        :return: The frame's height in pixels.
        :rtype: ``int``
        """
        require_tk("get_height", self)
        return self.widget.winfo_height()

    def get_width(self):
        """Get the frame's width.

        :return: The frame's width in pixels.
        :rtype: ``int``
        """
        require_tk("get_width", self)
        return self.widget.winfo_width()

    def set_background(self, background):
        """Set the frame's backgroundcolor.

        :param str background: The backgroundcolor. Must be any of
                               'white', 'black', 'red', 'green', 'blue',
                               'yellow', 'orange', 'grey', 'gray',
                               'pink', 'purple', or be a valid hex color
                               code.
        :raises TypeError: If ``background`` is not a string.
        :raises ValueError: If ``background`` is not a named color or a
                            valid hex color code.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_background", self)
        validate_color(background)
        self.widget.configure(
            background=constants.COLORS.get(background, background)
        )

    def set_height(self, height):
        """Set the frame's height.

        :param int height: The height in pixels. Must be at least 1.
        :raises TypeError: If ``height`` is not an integer.
        :raises ValueError: If ``height`` is less than 1.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_height", self)
        validate_height(height)
        self.widget.configure(height=height)

    def set_width(self, width):
        """Set the frame's width.

        :param int width: The width in pixels. Must be at least 1.
        :raises TypeError: If ``width`` is not an integer.
        :raises ValueError: If ``width`` is less than 1.
        :return: None.
        :rtype: ``None``
        """
        require_tk("set_width", self)
        validate_width(width)
        self.widget.configure(width=width)


class Text(TextWidget):
    """Represents a text element.

    :method __init__: Constructor.

    Superclass TextWidget
    =====================
    Represents a widget capable of displaying text.

    :method __init__: Constructor.
    :method get_align: Get the text's alignment.
    :method get_background: Get the backgroundcolor.
    :method get_foreground: Get the textcolor.
    :method get_value: Get the text value.
    :method set_align: Set the text's alignment.
    :method set_background: Set the backgroundcolor.
    :method set_foreground: Set the textcolor.
    :method set_value: Set the text value.

    Superclass Widget
    =================
    Represents a visual element.

    :method __init__: Constructor.
    :method destroy: Destroy the widget and its children.
    :method disable: Deactivate the widget.
    :method display: Display the widget.
    :method enable: Activate the widget.
    :method focus: Delegate focus to the widget.
    :method get_style: Get the widget's style.
    :method hide: Hide the widget.
    :method set_style: Set the widget's style.
    :property children: Get the widget's children.
    :property parent: Get the widget's parent.
    """

    def __init__(
                 self,
                 parent,
                 value="",
                 foreground="black",
                 background="white",
                 align="center"
                ):
        super(Text, self).__init__(
            parent=parent,
            wtype=tk.Label,
            value=value,
            foreground=foreground,
            background=background,
            align=align
        )


class Entry(TextWidget):
    """Represents an input field.

    :method __init__: Constructor.

    Superclass TextWidget
    =====================
    Represents a widget capable of displaying text.

    :method __init__: Constructor.
    :method get_align: Get the text's alignment.
    :method get_background: Get the backgroundcolor.
    :method get_foreground: Get the textcolor.
    :method get_value: Get the text value.
    :method set_align: Set the text's alignment.
    :method set_background: Set the backgroundcolor.
    :method set_foreground: Set the textcolor.
    :method set_value: Set the text value.

    Superclass Widget
    =================
    Represents a visual element.

    :method __init__: Constructor.
    :method destroy: Destroy the widget and its children.
    :method disable: Deactivate the widget.
    :method display: Display the widget.
    :method enable: Activate the widget.
    :method focus: Delegate focus to the widget.
    :method get_style: Get the widget's style.
    :method hide: Hide the widget.
    :method set_style: Set the widget's style.
    :property children: Get the widget's children.
    :property parent: Get the widget's parent.
    """

    def __init__(
                 self,
                 parent,
                 value="",
                 foreground="black",
                 background="white",
                 align="left"
                ):
        super(Entry, self).__init__(
            parent=parent,
            wtype=tk.Entry,
            value=value,
            foreground=foreground,
            background=background,
            align=align
        )


class Button(TextWidget):
    """Represents a button.

    :method __init__: Constructor.
    :method get_image: Get the image's path.
    :method set_image: Set the image's path.

    Superclass TextWidget
    =====================
    Represents a widget capable of displaying text.

    :method __init__: Constructor.
    :method get_align: Get the text's alignment.
    :method get_background: Get the backgroundcolor.
    :method get_foreground: Get the textcolor.
    :method get_value: Get the text value.
    :method set_align: Set the text's alignment.
    :method set_background: Set the backgroundcolor.
    :method set_foreground: Set the textcolor.
    :method set_value: Set the text value.

    Superclass Widget
    =================
    Represents a visual element.

    :method __init__: Constructor.
    :method destroy: Destroy the widget and its children.
    :method disable: Deactivate the widget.
    :method display: Display the widget.
    :method enable: Activate the widget.
    :method focus: Delegate focus to the widget.
    :method get_style: Get the widget's style.
    :method hide: Hide the widget.
    :method set_style: Set the widget's style.
    :property children: Get the widget's children.
    :property parent: Get the widget's parent.
    """

    def __init__(
                 self,
                 parent,
                 value="",
                 image=None,
                 foreground="black",
                 background="white",
                 align="center"
                ):
        if image is not None:
            validate_image(image)
            image_path = image
            image = load_photo_image(file=image)
        else:
            image_path = ""
        super(Button, self).__init__(
            parent=parent,
            wtype=tk.Button,
            value=value,
            image=image,
            image_path=image_path,
            foreground=foreground,
            background=background,
            justify=align
        )

    def get_image(self):
        require_tk("get_image", self)
        return self.widget.__image_path

    def set_image(self, image):
        require_tk("set_image", self)
        validate_image(image)
        image = load_photo_image(file=image)
        image_path = image
        self.widget.configure(image=image)
        self.widget.__image_path = image_path
        self.widget.__image_cache = image


class Image(Widget):
    """Represents an image.

    :method __init__: Constructor.
    :method get_height: Get the image's height.
    :method get_image: Get the image's path.
    :method get_width: Get the image's width.
    :method set_image: Set the image's path.

    Superclass Widget
    =================
    Represents a visual element.

    :method __init__: Constructor.
    :method destroy: Destroy the widget and its children.
    :method disable: Deactivate the widget.
    :method display: Display the widget.
    :method enable: Activate the widget.
    :method focus: Delegate focus to the widget.
    :method get_style: Get the widget's style.
    :method hide: Hide the widget.
    :method set_style: Set the widget's style.
    :property children: Get the widget's children.
    :property parent: Get the widget's parent.
    """

    def __init__(
                 self,
                 parent,
                 file
                ):
        validate_image(file)
        image = load_photo_image(file=file)
        super(Image, self).__init__(
            parent=parent,
            wtype=tk.label,
            image=image,
            image_path=file,
        )

    def get_height(self):
        """Get the image's height.

        :return: The image's height in pixels.
        :rtype: int
        """
        require_tk("get_height", self)
        return self.widget.__image_cache.height()

    def get_image(self):
        """Get the image's path.

        :return: The image's absolute path.
        :rtype: str
        """
        require_tk("get_image", self)
        return os.path.abspath(self.widget.__image_path)

    def get_width(self):
        """Get the image's width.

        :return: The image's width in pixels.
        :rtype: int
        """
        require_tk("get_width", self)
        return self.widget.__image_cache.width()

    def set_image(self, file):
        """Set the image's path.

        :return: None.
        :rtype: ``None``
        """
        require_tk("set_image", self)
        validate_image(file)
        image_path = file
        image = load_photo_image(file=image)
        self.widget.configure(image=image)
        self.widget.__image_path = image_path
        self.widget.__image_cache = image
