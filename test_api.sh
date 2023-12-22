#! /bin/bash

export FINAS_BACKEND_ENV=test &&
pytest -v . -W ignore::pytest.PytestCacheWarning &&
export FINAS_BACKEND_ENV=dev