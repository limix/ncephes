#!/usr/bin/env bash
set -e -x

if [ -z ${DOCKER_IMAGE+x} ]; then

    if [[ $TRAVIS_OS_NAME == 'linux' ]]; then
        python setup.py sdist
        if [ "${NUMBA}" == "true" ]; then
            pip install dist/`ls dist | grep -i -E '\.(gz)$' | head -1`[numba]
        else
            pip install dist/`ls dist | grep -i -E '\.(gz)$' | head -1`;
        fi
        pushd /
        python -c "import sys; import ncephes; sys.exit(ncephes.test())"
        popd
    else
        pip install --upgrade pip
        pip install wheel setuptools
        python setup.py bdist_wheel
        ls dist
    fi
else
    docker run --rm -v `pwd`:/io $DOCKER_IMAGE /io/travis/build_wheels.sh
    ls wheelhouse/
fi
