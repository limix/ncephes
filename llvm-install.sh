#!/bin/bash

cat >> /etc/apt/sources.list << LLVMAPT
# LLVM
deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty main
deb-src http://apt.llvm.org/trusty/ llvm-toolchain-trusty main
# 3.7
deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty-3.7 main
deb-src http://apt.llvm.org/trusty/ llvm-toolchain-trusty-3.7 main
LLVMAPT

wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -
apt-get install clang-3.7 clang-3.7-doc libclang-common-3.7-dev \
                libclang-3.7-dev libclang1-3.7 libclang1-3.7-dbg \
                libllvm-3.7-ocaml-dev libllvm3.7 libllvm3.7-dbg lldb-3.7 \
                llvm-3.7 llvm-3.7-dev llvm-3.7-doc llvm-3.7-examples \
                llvm-3.7-runtime clang-modernize-3.7 clang-format-3.7 \
                python-clang-3.7 lldb-3.7-dev
