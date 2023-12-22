#! /bin/bash

export ZYWA_ENV=test &&
pytest -v . -W ignore::pytest.PytestCacheWarning &&
export ZYWA_ENV=dev