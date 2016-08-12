import os


def get_include():
    """
    Return the directory that contains the nCephes \\*.h header files.
    Extension modules that need to compile against nCephes should use this
    function to locate the appropriate include directory.
    Notes
    -----
    When using ``distutils``, for example in ``setup.py``.
    ::
        import ncephes as nc
        ...
        Extension('extension_name', ...
                include_dirs=[nc.get_include()])
        ...
    """
    import ncephes
    d = os.path.join(os.path.dirname(ncephes.__file__), 'include')
    return d


def get_lib():
    import ncephes
    d = os.path.join(os.path.dirname(ncephes.__file__), 'lib')
    return d
