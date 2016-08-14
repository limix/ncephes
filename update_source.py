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
from build_helpers import get_info


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


def apply_patch():
    cmd = "patch ncephes/cephes/cprob/gamma.c ncephes/cephes/gamma.patch"
    subprocess.check_call(cmd, shell=True)
    cmd = "patch ncephes/cephes/cprob/incbet.c ncephes/cephes/incbet.patch"
    subprocess.check_call(cmd, shell=True)


def _create_api(module):
    d = get_info(module)
    h = module.upper() + '_H'

    guard_start = "#ifndef %s\n#define %s\n\n" % (h, h)
    guard_end = "\n\n#endif\n"
    apidecls = '\n'.join(['extern ' + f for f in d['apidecls']])
    with open(join('ncephes', 'include', 'ncephes', module + '.h'), 'w') as f:
        f.write(guard_start + apidecls + guard_end)

    with open(join('ncephes', 'cephes', module + '_ffcall.c'), 'w') as f:
        t = ('#include "ncephes/' + module + '.h"\n\n'
             + '\n'.join(d['ffcalls']) + '\n\n')
        f.write(t)


def create_api():
    _create_api('cprob')
    _create_api('ellf')


def update():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        download_extract()
        clear_code()
        convert_old_style_proto()
        apply_patch()
        create_api()
    finally:
        os.chdir(old_path)

    print("Finished.")

if __name__ == '__main__':
    update()
