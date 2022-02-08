###############
Automated Tests
###############
--------------------------------------
Manual for developers and contributors
--------------------------------------

This command permit to run all tests and produce a very good report::

  pytest --cov-report term-missing:skip-covered --cov-fail-under=67 --cov=cc_codechecker tests/

Produce human readable reports with this command::

  pytest --cov-report html --cov=cc_codechecker tests/

This is the command used in ci, since we don't need terminal reports::

  pytest --cov-report= --cov=cc_codechecker tests/
