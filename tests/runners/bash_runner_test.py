"""Test Bash Runner methods."""

# Standard Library
from argparse import Namespace
from unittest.mock import MagicMock, patch

import pytest

# Codechecker
from cc_codechecker.context import Context
from cc_codechecker.runners.bash import Bash


@pytest.fixture(name='bash_runner')
def fixture_bash_runner() -> Bash:
  """Produce common Bash Runner."""
  context = Context(Namespace(verbose = True))
  yield Bash()
  del context

@patch('cc_codechecker.runners.bash.subprocess.check_output')
def test_position_bash(check: MagicMock, bash_runner: Bash):
  """Test returning position value."""
  check.return_value = '/usr/bin/bash'
  pos = bash_runner.position()
  assert pos

@patch('cc_codechecker.runners.bash.subprocess.check_output')
def test_position_value_error(check: MagicMock, bash_runner: Bash):
  """Test a missing bash runner."""
  check.return_value = ''
  pos = bash_runner.position()
  assert not pos

@patch('cc_codechecker.runners.bash.subprocess.check_output')
@patch('cc_codechecker.runners.bash.Bash.position')
def test_version_return(pos: MagicMock, run: MagicMock, bash_runner: Bash):
  """Test the version returned."""
  pos.return_value = 'pos'
  run.return_value = '1.0.0'
  ver = bash_runner.version()
  assert '1.0.0' == ver

@patch('cc_codechecker.runners.bash.subprocess.check_output')
@patch('cc_codechecker.runners.bash.Bash.position')
def test_check_position_value_error(
  pos: MagicMock,
  run: MagicMock,
  bash_runner: Bash,
):
  """Test the check position value error raised."""
  pos.return_value = ''
  run.return_value = '1.0.0'
  with pytest.raises(ValueError) as v_err:
    bash_runner.version()

  assert v_err.errisinstance(ValueError)
  assert v_err.match('Bash executable not installed')

@patch('cc_codechecker.runners.bash.subprocess.run')
@patch('cc_codechecker.runners.bash.Bash._check_position')
def test_run_return(check: MagicMock, run: MagicMock, bash_runner: Bash):
  """Test the execution returned."""
  check.return_value = 'pos'
  run.return_value = MagicMock(returncode=1, stdout='')
  result = bash_runner.run()
  assert (1, '') == result
