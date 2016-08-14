import sys
import contextlib
from setuptools.command.test import test as _TestCmd
from setuptools.extern import six
from pkg_resources import normalize_path
from pkg_resources import working_set
from pkg_resources import add_activation_listener
from pkg_resources import require


class TestCmd(_TestCmd):

    @contextlib.contextmanager
    def project_on_sys_path(self):

        with_2to3 = six.PY3 and getattr(self.distribution, 'use_2to3', False)
        sys.exit(1)

        if with_2to3:
            # If we run 2to3 we can not do this inplace:

            # Ensure metadata is up-to-date
            self.reinitialize_command('build_py', inplace=0)
            self.run_command('build_py')
            bpy_cmd = self.get_finalized_command("build_py")
            build_path = normalize_path(bpy_cmd.build_lib)

            # Build extensions
            self.reinitialize_command('egg_info', egg_base=build_path)
            self.run_command('egg_info')

            self.reinitialize_command('build_ext', inplace=0)
            self.run_command('build_ext')
        else:
            # Without 2to3 inplace works fine:
            self.run_command('egg_info')

            # Build extensions in-place
            self.reinitialize_command('build_ext', inplace=1)
            self.run_command('build_ext')

        ei_cmd = self.get_finalized_command("egg_info")

        old_path = sys.path[:]
        old_modules = sys.modules.copy()

        try:
            sys.path.insert(0, normalize_path(ei_cmd.egg_base))
            working_set.__init__()
            add_activation_listener(lambda dist: dist.activate())
            require('%s==%s' % (ei_cmd.egg_name, ei_cmd.egg_version))
            yield
        finally:
            sys.path[:] = old_path
            sys.modules.clear()
            sys.modules.update(old_modules)
            working_set.__init__()
