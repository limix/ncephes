import os

from setuptools import Command


def _show_compilers():
    from distutils.ccompiler import show_compilers as sc
    sc()


class build_capi(Command, object):

    description = "build C/C++ libraries"

    user_options = [
        ('build-clib', 'b',
         "directory to build C/C++ libraries to"),
        ('build-temp', 't',
         "directory to put temporary build by-products"),
        ('debug', 'g',
         "compile with debugging information"),
        ('force', 'f',
         "forcibly build everything (ignore file timestamps)"),
        ('compiler=', 'c',
         "specify the compiler type"),
    ]

    boolean_options = ['debug', 'force']

    help_options = [
        ('help-compiler', None,
         "list available compilers", _show_compilers),
    ]

    def __init__(self, *args, **kwargs):
        self.build_clib = None
        self.build_temp = None

        # List of libraries to build
        self.capi_libs = None

        # Compilation options for all libraries
        self.include_dirs = None
        self.define = []
        self.undef = []
        self.debug = None
        self.force = 0
        self.compiler = None
        super(build_capi, self).__init__(*args, **kwargs)

    def initialize_options(self):
        from build_helpers import get_libs_info
        dlib = get_libs_info()

        self.build_clib = None
        self.build_temp = None

        # List of libraries to build
        self.capi_libs = dlib['libraries']

        # Compilation options for all libraries
        self.include_dirs = None
        self.define = []
        self.undef = []
        self.debug = None
        self.force = 0
        self.compiler = None

    def finalize_options(self):
        # This might be confusing: both build-clib and build-temp default
        # to build-temp as defined by the "build" command.  This is because
        # I think that C libraries are really just temporary build
        # by-products, at least from the point of view of building Python
        # extensions -- but I want to keep my options open.
        self.set_undefined_options('build',
                                   ('build_temp', 'build_clib'),
                                   ('build_temp', 'build_temp'),
                                   ('compiler', 'compiler'),
                                   ('debug', 'debug'),
                                   ('force', 'force'))

        # self.capi_libs = self.distribution.capi_libs
        if self.capi_libs:
            self.check_library_list(self.capi_libs)

        if self.include_dirs is None:
            self.include_dirs = self.distribution.include_dirs or []
        if isinstance(self.include_dirs, str):
            self.include_dirs = self.include_dirs.split(os.pathsep)

    def run(self):
        from distutils.ccompiler import customize_compiler
        if not self.capi_libs:
            return

        # Yech -- this is cut 'n pasted from build_ext.py!
        from distutils.ccompiler import new_compiler
        self.compiler = new_compiler(compiler=self.compiler,
                                     dry_run=self.dry_run,
                                     force=self.force)

        customize_compiler(self.compiler)

        if self.include_dirs is not None:
            self.compiler.set_include_dirs(self.include_dirs)
        if self.define is not None:
            # 'define' option is a list of (name,value) tuples
            for (name, value) in self.define:
                self.compiler.define_macro(name, value)
        if self.undef is not None:
            for macro in self.undef:
                self.compiler.undefine_macro(macro)

        self.build_libraries(self.capi_libs)

    def check_library_list(self, capi_libs):
        """Ensure that the list of libraries is valid.

        `library` is presumably provided as a command option 'libraries'.
        This method checks that it is a list of 2-tuples, where the tuples
        are (library_name, build_info_dict).

        Raise DistutilsSetupError if the structure is invalid anywhere;
        just returns otherwise.
        """
        from distutils.errors import DistutilsSetupError
        if not isinstance(capi_libs, list):
            raise DistutilsSetupError, \
                "'libraries' option must be a list of tuples"

        for lib in capi_libs:
            if not isinstance(lib, tuple) and len(lib) != 2:
                raise DistutilsSetupError, \
                    "each element of 'libraries' must a 2-tuple"

            name, build_info = lib

            if not isinstance(name, str):
                raise DistutilsSetupError, \
                    "first element of each tuple in 'libraries' " + \
                    "must be a string (the library name)"
            if '/' in name or (os.sep != '/' and os.sep in name):
                raise DistutilsSetupError, \
                    ("bad library name '%s': " +
                     "may not contain directory separators") % \
                    lib[0]

            if not isinstance(build_info, dict):
                raise DistutilsSetupError, \
                    "second element of each tuple in 'libraries' " + \
                    "must be a dictionary (build info)"

    def get_library_names(self):
        # Assume the library list is valid -- 'check_library_list()' is
        # called from 'finalize_options()', so it should be!
        if not self.capi_libs:
            return None

        lib_names = []
        for (lib_name, _) in self.capi_libs:
            lib_names.append(lib_name)
        return lib_names

    def get_source_files(self):
        from distutils.errors import DistutilsSetupError
        self.check_library_list(self.capi_libs)
        filenames = []
        for (lib_name, build_info) in self.capi_libs:
            sources = build_info.get('sources')
            if sources is None or not isinstance(sources, (list, tuple)):
                raise DistutilsSetupError, \
                    ("in 'libraries' option (library '%s'), "
                     "'sources' must be present and must be "
                     "a list of source filenames") % lib_name

            filenames.extend(sources)
        return filenames

    def build_libraries(self, capi_libs):
        import ipdb
        ipdb.set_trace()
        from distutils.errors import DistutilsSetupError
        for (lib_name, build_info) in capi_libs:
            sources = build_info.get('sources')
            if sources is None or not isinstance(sources, (list, tuple)):
                raise DistutilsSetupError, \
                    ("in 'libraries' option (library '%s'), " +
                     "'sources' must be present and must be " +
                     "a list of source filenames") % lib_name
            sources = list(sources)

            from distutils import log
            log.info("building '%s' library", lib_name)

            # First, compile the source code to object files in the library
            # directory.  (This should probably change to putting object
            # files in a temporary build directory.)
            macros = build_info.get('macros')
            include_dirs = build_info.get('include_dirs')
            objects = self.compiler.compile(sources,
                                            output_dir=self.build_temp,
                                            macros=macros,
                                            include_dirs=include_dirs,
                                            debug=self.debug)

            # Now "link" the object files together into a static library.
            # (On Unix at least, this isn't really linking -- it just
            # builds an archive.  Whatever.)
            self.compiler.create_static_lib(objects, lib_name,
                                            output_dir=self.build_clib,
                                            debug=self.debug)
