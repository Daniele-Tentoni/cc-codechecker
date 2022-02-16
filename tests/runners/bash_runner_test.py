"""Test Bash Runner methods."""

# Standard Library
from unittest.mock import MagicMock, patch

import pytest

# Codechecker
from cc_codechecker.runners.bash import Bash


@pytest.fixture(name='bash_runner')
def fixture_bash_runner() -> Bash:
  """Produce common Bash Runner."""
  return Bash()

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
