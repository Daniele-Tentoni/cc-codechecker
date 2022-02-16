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

Additional notes
################

You can run tests using Poetry and Python Module execution using::

  poetry run python -m pytest --cov-report html term-missing:skip-covered --cov-fail-under=67 --cov=cc_codechecker tests/

If you are already inside the virtual environment managed by Poetry (and you had run ``poetry shell``), you could use::

  python -m pytest --cov-report html term-missing:skip-covered --cov-fail-under=67 --cov=cc_codechecker tests/

If you want to run Pytest without Python Module execution, run::

  pytest --cov-report html term-missing:skip-covered --cov-fail-under=67 --cov=cc_codechecker tests/
