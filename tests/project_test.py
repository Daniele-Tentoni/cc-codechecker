"""Unit tests for Projects."""

# Standard Library
from argparse import Namespace
from unittest.mock import patch

import pytest

# Codechecker
from cc_codechecker.context import Context
from cc_codechecker.project import Project


@pytest.fixture(name='project')
def fixture_project():
  context = Context(Namespace(verbose = True))
  yield Project('bash')
  del context

def test_project():
  context = Context(Namespace(verbose = True))
  with patch('builtins.print') as printer:
    Project('bash')
  printer.assert_called_once_with('Adding Project bash')
  del context

def test_verbose_project():
  context = Context(Namespace(verbose = False))
  with patch('builtins.print') as printer:
    Project('bash', verbose = True)
  printer.assert_called_once_with('Adding Project cash')
  del context

def test_not_verbose_project():
  context = Context(Namespace(verbose = True))
  with patch('builtins.print') as printer:
    Project('csharp', verbose = False)
  printer.assert_not_called()
  del context
