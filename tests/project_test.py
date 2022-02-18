# SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com
#
# SPDX-License-Identifier: MIT

"""Unit tests for Projects."""

# Standard Library
from argparse import Namespace
from unittest.mock import MagicMock, patch

import pytest

# Codechecker
from cc_codechecker.context import Context
from cc_codechecker.project import Project


@pytest.fixture(name='project')
def fixture_project():
  """Provide common Project instance."""
  context = Context(Namespace(verbose = False))
  yield Project('bash')
  del context

def test_project():
  """Test right verbosity given in the context."""
  context = Context(Namespace(verbose = True))
  with patch('builtins.print') as printer:
    Project('bash')
  printer.assert_called_once_with('Adding Project bash')
  del context

def test_verbose_project():
  """Test right verbosity given in the constructor."""
  context = Context(Namespace(verbose = False))
  with patch('builtins.print') as printer:
    Project('bash', verbose = True)
  printer.assert_called_once_with('Adding Project bash')
  del context

def test_not_verbose_project():
  """Test right verbosity given in the constructor."""
  context = Context(Namespace(verbose = True))
  with patch('builtins.print') as printer:
    Project('csharp', verbose = False)
  printer.assert_not_called()
  del context

@patch('cc_codechecker.runners.bash.Bash.version')
def test_version(version: MagicMock, project: Project):
  """Test right version provided from runner."""
  version.return_value = '1.0.0'
  ver = project.version()
  assert not ver

@patch('cc_codechecker.project.Project.version')
@patch('cc_codechecker.runner.Runner.run')
def test_run(version: MagicMock, runner: MagicMock, project: Project):
  """Test project successful run."""
  version.return_value = True
  runner.return_value = MagicMock(
    returncode=0,
    stdout='',
  )
  run = project.run(None)
  assert run[0] == 0
  assert run[1] == ''

@patch('cc_codechecker.project.Project.version')
def test_run_version_check_fail(version: MagicMock, project: Project):
  """Test project run."""
  version.return_value = False
  run = project.run(None)
  assert run[0] == -1
  assert run[1] == 'Unknown version'
