#!/bin/bash
set -e -x

yum install -y atlas-devel libffi libffi-devel

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    if [[ $PYBIN == *"p26"* ]]; then
        continue
    fi
    if [[ $PYBIN == *"p33"* ]]; then
        continue
    fi
    "${PYBIN}/pip" install Cython numpy
    "${PYBIN}/pip" wheel /io/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    auditwheel repair "$whl" -w /io/wheelhouse/
done

# Install packages and test
for PYBIN in /opt/python/*/bin/; do
    if [[ $PYBIN == *"p26"* ]]; then
        continue
    fi
    if [[ $PYBIN == *"p33"* ]]; then
        continue
    fi
    "${PYBIN}/pip" install ncephes --no-index -f /io/wheelhouse
    (cd "$HOME"; "${PYBIN}/nosetests" ncephes)
done
