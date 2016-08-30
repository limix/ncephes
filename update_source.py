from six.moves.urllib.request import urlopen
import sys
import shutil
import os
from os import listdir
from os.path import join
from os.path import isdir
from os.path import splitext
import re
import tarfile
import subprocess
from build_helpers import get_supported_modules
from build_helpers import api_fdecls
from build_helpers import forward_call
from module_info import get_fdecls


SUPPORTED_MODULES = open('./supported_modules.txt').read().split("\n")[:-1]


def download_extract():
    url = "http://www.netlib.org/cephes/"
    print("Downloading...")
    page = urlopen(url).read()

    c = re.compile(r'"([^"]+\.tgz)"')
    pkgs = re.findall(c, page)
    pkgs = [p for p in pkgs if splitext(p)[0] in SUPPORTED_MODULES]

    print("Extracting...")
    for pkg in pkgs:
        stream = urlopen(url + pkg)
        content = tarfile.open(fileobj=stream, mode="r|gz")
        name = splitext(pkg)[0]
        path = join('ncephes', 'cephes', name)
        if os.path.exists(path):
            shutil.rmtree(path)
        if name == 'c9x-complex':
            content.extractall(join('ncephes', 'cephes'))
        else:
            content.extractall(path)

    subprocess.check_call('chmod -R u+rw ncephes/cephes/', shell=True)
    subprocess.check_call('chmod -R go+r ncephes/cephes/', shell=True)


def clear_code():
    print("Cleaning files...")
    root = join('ncephes', 'cephes')
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        for f in listdir(join(root, d)):
            fp = join(root, d, f)
            cmd = "perl -i -pe 's/[\x0c]//g' %s" % fp
            subprocess.check_call(cmd, shell=True)
            if fp.endswith('.c') or fp.endswith('.h'):
                cmd = "perl -i -pe 's/(ncephes_)*cabs/ncephes_cabs/g' %s" % fp
                subprocess.check_call(cmd, shell=True)
                cmd = "perl -i -pe 's/(ncephes_)*csqrt/ncephes_csqrt/g' %s" % fp
                subprocess.check_call(cmd, shell=True)
                if f != 'gamma.c' and f != 'incbet.c':
                    cmd = "perl -i -pe 's/(cephes_)*gamma/cephes_gamma/g' %s" % fp
                    subprocess.check_call(cmd, shell=True)


def ncephes_consts():
    print("Setting ncephes consts...")
    root = join('ncephes', 'cephes')
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        for f in listdir(join(root, d)):
            fp = join(root, d, f)
            if fp.endswith('.c') or fp.endswith('.h'):
                cmd = "perl -i -pe 's/(NCEPHES_)*INFINITY/NCEPHES_INF/g' %s" % fp
                subprocess.check_call(cmd, shell=True)
                cmd = "perl -i -pe 's/(NCEPHES_)*NAN/NCEPHES_NAN/g' %s" % fp
                subprocess.check_call(cmd, shell=True)
                cmd = "perl -i -pe 's/(NCEPHES_)*MAXNUM/NCEPHES_MAXNUM/g' %s" % fp
                subprocess.check_call(cmd, shell=True)
                cmd = "perl -i -pe 's/(NCEPHES_)*PI/NCEPHES_PI/g' %s" % fp
                subprocess.check_call(cmd, shell=True)


def convert_old_style_proto():
    print("Converting K&R to ANSI style for function declaration...")
    root = join('ncephes', 'cephes')
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        if d not in SUPPORTED_MODULES:
            continue
        for f in listdir(join(root, d)):
            if not (f.endswith('.c') or f.endswith('.h')):
                continue
            fp = join(root, d, f)
            incl1 = join(os.getcwd(), root, d)
            incl2 = join(os.getcwd(), root)
            cmd = "cproto -q -I%s -I%s -a %s" % (incl1, incl2, fp)
            subprocess.check_call(cmd, shell=True)


def _unlink(f):
    if os.path.exists(f):
        os.unlink(f)


def apply_patch():
    cmd = "patch ncephes/cephes/polyn/polyn.c ncephes/cephes/polyn.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/polyn/polyn.c ncephes/cephes/polyn.2.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/polyn/polmisc.c ncephes/cephes/polmisc.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/polyn/polmisc.c ncephes/cephes/polmisc.2.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/cprob/gamma.c ncephes/cephes/gamma.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/cprob/gamma.c ncephes/cephes/gamma.2.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/cprob/gamma.c ncephes/cephes/gamma.3.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/cprob/gamma.c ncephes/cephes/gamma.4.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/misc/beta.c ncephes/cephes/beta.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/misc/beta.c ncephes/cephes/beta.2.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/misc/beta.c ncephes/cephes/beta.3.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/cprob/incbet.c ncephes/cephes/incbet.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/ellf/ellf.c ncephes/cephes/ellf.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/misc/revers.c ncephes/cephes/revers.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/polyn/revers.c ncephes/cephes/revers.2.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/polyn/revers.c ncephes/cephes/revers.3.patch"
    subprocess.check_call(cmd, shell=True)
    _unlink('ncephes/cephes/cmath/atan.c')
    _unlink('ncephes/cephes/cmath/exp.c')
    _unlink('ncephes/cephes/eval/protos.h')

    _unlink('ncephes/cephes/cprob/const.c')
    _unlink('ncephes/cephes/ellf/const.c')
    _unlink('ncephes/cephes/cmath/const.c')

    _unlink('ncephes/cephes/cprob/mconf.h')
    _unlink('ncephes/cephes/ellf/mconf.h')
    _unlink('ncephes/cephes/cmath/mconf.h')
    _unlink('ncephes/cephes/eval/mconf.h')

    _unlink('ncephes/cephes/polyn/polyr.c')

    _unlink('ncephes/cephes/cprob/mtherr.c')
    _unlink('ncephes/cephes/ellf/mtherr.c')
    _unlink('ncephes/cephes/cmath/mtherr.c')
    _unlink('ncephes/cephes/eval/mtherr.c')
    _unlink('ncephes/cephes/misc/mtherr.c')


def _create_api(module):
    h = module.upper() + '_H'
    fdecls = get_fdecls(module)
    apidecls = [api_fdecls(f) for f in fdecls]
    ffcalls = [forward_call(f) for f in fdecls]

    guard_start = "#ifndef %s\n#define %s\n\n" % (h, h)
    guard_end = "\n\n#endif\n"
    apidecls = '\n'.join(apidecls)
    with open(join('ncephes', 'include', 'ncephes', module + '.h'), 'w') as f:
        f.write(guard_start + apidecls + guard_end)

    with open(join('ncephes', 'cephes', module + '_ffcall.c'), 'w') as f:
        f.write('#include "ncephes/' + module + '.h"\n\n')
        if len(apidecls) == 0:
            f.write('int _do_nothing_%s() { return 0; }' % module)
        else:
            f.write('\n'.join(fdecls) + '\n\n')
            f.write('\n'.join(ffcalls) + '\n\n')


def create_api():
    modules = get_supported_modules()
    for module in modules:
        _create_api(module)


def update():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        download_extract()
        clear_code()
        convert_old_style_proto()
        apply_patch()
        ncephes_consts()
        create_api()
    finally:
        os.chdir(old_path)

    print("Finished.")

if __name__ == '__main__':
    update()
