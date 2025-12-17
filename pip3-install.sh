#!/bin/bash
pip3 uninstall -y -r <(pip3 freeze | grep -v my-package)

pip3 install --upgrade pip

#pip3 install \
# google-cloud-bigquery \
# --constraint constraints.txt

# MacBook M3 & M4
#       AttributeError: cython_sources
 pip3 install "cython<3.0.0" wheel

# ext_modules=cythonize([
#          import numpy
#      ModuleNotFoundError: No module named 'numpy'
pip3 install numpy --constraint constraints.txt

#      AttributeError: cython_sources
#pip3 install "pyyaml==5.4.1" --no-build-isolation
pip3 install pyyaml --no-build-isolation --constraint constraints.txt

pip3 install \
 -r requirements.txt \
 --constraint constraints.txt
