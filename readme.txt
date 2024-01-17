brew install pyenv pyenv-virtualenv

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.8.14

pyenv virtualenv 3.8.14 composer2
pyenv activate composer2

./pip3-install.sh
#Installing collected packages: pyasn1, urllib3, six, rsa, pyasn1-modules, protobuf, packaging, idna, grpcio, google-crc32c, charset-normalizer, certifi, cachetools, requests, python-dateutil, proto-plus, googleapis-common-protos, google-resumable-media, google-auth, grpcio-status, google-api-core, google-cloud-core, google-cloud-bigquery
#Successfully installed cachetools-5.3.0 certifi-2022.12.7 charset-normalizer-3.1.0 google-api-core-2.11.1 google-auth-2.17.0 google-cloud-bigquery-3.11.4 google-cloud-core-2.3.3 google-crc32c-1.5.0 google-resumable-media-2.6.0 googleapis-common-protos-1.60.0 grpcio-1.57.0 grpcio-status-1.57.0 idna-3.4 packaging-23.0 proto-plus-1.22.3 protobuf-4.23.4 pyasn1-0.4.8 pyasn1-modules-0.2.8 python-dateutil-2.8.2 requests-2.28.2 rsa-4.9 six-1.16.0 urllib3-1.26.15