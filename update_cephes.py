from six.moves.urllib.request import urlopen
import shutil
import os
import re
import tarfile

url = "http://www.netlib.org/cephes/"
page = urlopen(url).read()

c = re.compile(r'"([^"]+\.tgz)"')
pkgs = re.findall(c, page)
pkgs = [pkg for pkg in pkgs if pkg != '128bit.tgz']

curdir = os.path.abspath(os.path.dirname(__file__))

for pkg in pkgs:
    # content = urllib.urlopen(url + pkg).read()
    stream = urlopen(url + pkg)
    content = tarfile.open(fileobj=stream, mode="r|gz")
    name = os.path.splitext(pkg)[0]
    path = os.path.join(curdir, 'ncephes', 'cephes', name)
    if os.path.exists(path):
        shutil.rmtree(path)
    content.extractall(path)
