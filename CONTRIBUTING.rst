============
Contributing
============
---------------------------------------------------------------------------------
This document describes contribution guidelines that are specific to Codechecker.
---------------------------------------------------------------------------------

Thank you for your interest in contributing to Codechecker! There are many ways to contribute and we appreciate all of them.

Please make sure to read the relevant section before making your contribution! It will make it a lot easier for us maintainers to make the most of it and smooth out the experience for all involved. green_heart

This project is in developing, so check back later, we will populate those contributing guidelines soon.

Request support
---------------

If you have a question about the project, how to use it or just need clarification about something:

* Open an issue
* Provide as much context as you can
* Provide a useful label

Please avoid filling new issues as extensions of one you already made.

Report an error
---------------

If you run into an error or bug:

* Open an issue
* Include *reproduction steps* that someone else can follow to reproduce the error on their own
* Provide a useful label: use *critical* label only if the problem described makes the code completely unusable in a common situation

If you have created a coding challenge that reproduce this problem, link it! It will be appreciated.

Request a feature
-----------------

If the project doesn't do something you need or want it to do:

* Open an issue
* Provide as much context as you can about what you're running into
* Please try and be clear about why existing features and alternatives would not work for you

Contribute code
---------------

We like code commits a lot! They're super handy, and they keep the project going and doing the work it needs to do to be useful to others.

Be sure to include relevant tests for the code being added or changed. Contributions without accompanying tests will be held off until a test is added, unless the maintainers consider the specific tests to be either impossible, or way too much of a burden for such a contribution.

Project setup
~~~~~~~~~~~~~

So you wanna contribute some code! That's great!

* Fork this repository to your github account
* Install Poetry as dependency manager for Python
* Run ``poetry install`` to install dependencies
* Run ``pre-commit autoupdate``
* Run ``poetry shell`` to open the venv for the project and ``code .`` to start a new session of vscode inside that venv
* Run test suite using ``pytest``

Make a change
~~~~~~~~~~~~~

* Write tests that verify that your contribution works as expected
* Make any necessary changes to the source code
* Include any additional documentation the changes might need
* Write clear, concise commit message(s) using Semantic Commit Message Format
* If no pre-commit hooks was executed, run ``pre-commit run --all-files``
* Open a new pr with your changes

Core Team Members
-----------------

Daniele Tentoni <daniele.tentoni.1996@gmail.com>

Proposed features
-------------

1. Generate an 8 digit hash for Challenges without a name to identify them in logs
   This feature can help debugging program and make output cleaner.
