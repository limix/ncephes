import os
import string

from setuptools import Command

from build_helpers import get_supported_modules
from capi_info import get_capi_module_name
from capi_info import get_sources
from module_info import get_extra_compile_args
from capi_info import get_include_dirs


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
        ('inplace', 'i',
         "ignore build-lib and put compiled extensions into the source " +
         "directory alongside your pure Python modules"),
    ]

    boolean_options = ['inplace', 'debug', 'force']

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
        self.inplace = 0
        self.compiler = None
        super(build_capi, self).__init__(*args, **kwargs)

    def initialize_options(self):

        self.build_clib = None
        self.build_temp = None
        self.capi_libs = []

        modules = get_supported_modules()
        for module in modules:
            sources = get_sources(module)
            incl = get_include_dirs(module)
            eca = get_extra_compile_args()
            m = get_capi_module_name(module)
            self.capi_libs.append((m, {'sources': sources,
                                       'include_dirs': incl,
                                       'extra_compile_args': eca}))

        # Compilation options for all libraries
        self.include_dirs = None
        self.define = []
        self.undef = []
        self.debug = None
        self.force = 0
        self.inplace = 0
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
            raise DistutilsSetupError("'libraries' option must" +
                                      " be a list of tuples")

        for lib in capi_libs:
            if not isinstance(lib, tuple) and len(lib) != 2:
                raise DistutilsSetupError("each element of 'libraries' " +
                                          "must a 2-tuple")

            name, build_info = lib

            if not isinstance(name, str):
                raise DistutilsSetupError(
                    "first element of each tuple in 'libraries' " +
                    "must be a string (the library name)")
            if '/' in name or (os.sep != '/' and os.sep in name):
                raise DistutilsSetupError(
                    ("bad library name '%s': " +
                     "may not contain directory separators") %
                    lib[0])

            if not isinstance(build_info, dict):
                raise DistutilsSetupError(
                    "second element of each tuple in 'libraries' " +
                    "must be a dictionary (build info)")

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
                raise DistutilsSetupError(
                    ("in 'libraries' option (library '%s'), "
                     "'sources' must be present and must be "
                     "a list of source filenames") % lib_name)

            filenames.extend(sources)
        return filenames

    def build_libraries(self, capi_libs):
        from distutils.errors import DistutilsSetupError
        for (lib_name, build_info) in capi_libs:
            sources = build_info.get('sources')
            if sources is None or not isinstance(sources, (list, tuple)):
                raise DistutilsSetupError(
                    ("in 'libraries' option (library '%s'), " +
                     "'sources' must be present and must be " +
                     "a list of source filenames") % lib_name)
            sources = list(sources)

            from distutils import log
            log.info("building '%s' library", lib_name)

            # First, compile the source code to object files in the library
            # directory.  (This should probably change to putting object
            # files in a temporary build directory.)
            macros = build_info.get('macros')
            include_dirs = build_info.get('include_dirs')
            eca = build_info.get('extra_compile_args')
            objects = self.compiler.compile(sources,
                                            output_dir=self.build_temp,
                                            macros=macros,
                                            include_dirs=include_dirs,
                                            debug=self.debug,
                                            extra_preargs=eca)

            # Now "link" the object files together into a static library.
            # (On Unix at least, this isn't really linking -- it just
            # builds an archive.  Whatever.)
            lib_name = self.get_ext_fullpath(lib_name)
            self.compiler.create_static_lib(objects, lib_name,
                                            output_dir=self.build_clib,
                                            debug=self.debug)

    def get_ext_fullpath(self, ext_name):
        """Returns the path of the filename for a given extension.

        The file is located in `build_lib` or directly in the package
        (inplace option).
        """
        # makes sure the extension name is only using dots
        all_dots = string.maketrans('/' + os.sep, '..')
        ext_name = ext_name.translate(all_dots)

        fullname = self.get_ext_fullname(ext_name)
        modpath = fullname.split('.')
        filename = self.get_ext_filename(ext_name)
        filename = os.path.split(filename)[-1]

        if not self.inplace:
            # no further work needed
            # returning :
            #   build_dir/package/path/filename
            filename = os.path.join(*modpath[:-1] + [filename])
            return os.path.join(self.build_clib, filename)

        # the inplace option requires to find the package directory
        # using the build_py command for that
        package = '.'.join(modpath[0:-1])
        build_py = self.get_finalized_command('build_py')
        package_dir = os.path.abspath(build_py.get_package_dir(package))

        # returning
        #   package_dir/filename
        return os.path.join(package_dir, filename)

    def get_ext_fullname(self, ext_name):
        """Returns the fullname of a given extension name.

        Adds the `package.` prefix"""
        if not hasattr(self, 'package') or self.package is None:
            return ext_name
        else:
            return self.package + '.' + ext_name

    def get_ext_filename(self, ext_name):
        r"""Convert the name of an extension (eg. "foo.bar") into the name
        of the file from which it will be loaded (eg. "foo/bar.so", or
        "foo\bar.pyd").
        """
        ext_path = string.split(ext_name, '.')
        # OS/2 has an 8 character module (extension) limit :-(
        if os.name == "os2":
            ext_path[len(ext_path) - 1] = ext_path[len(ext_path) - 1][:8]
        # so_ext = self.compiler.static_lib_extension
        so_ext = ''
        if os.name == 'nt' and self.debug:
            return os.path.join(*ext_path) + '_d' + so_ext
        return os.path.join(*ext_path) + so_ext
