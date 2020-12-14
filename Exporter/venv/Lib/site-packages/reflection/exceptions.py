class TkinterException(Exception, object):
    """Exception.
    Raised when tk.TclError is raised and no further information is
    available to handle the exception.
    """
    pass
