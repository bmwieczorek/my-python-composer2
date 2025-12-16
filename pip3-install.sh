#!/bin/bash
pip3 uninstall -y -r <(pip3 freeze)

pip3 install --upgrade pip

#pip3 install \
# google-cloud-bigquery \
# --constraint constraints.txt

# mackbookair issue - needs Cython==0.29.37
# pip3 install "cython<3.0.0" wheel
# pip3 install "pyyaml==5.4.1" --no-build-isolation
# pip3 install "numpy==1.24.2"

pip3 install \
 -r requirements.txt \
 --constraint constraints.txt
