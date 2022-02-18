# SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com
#
# SPDX-License-Identifier: MIT

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

@patch('cc_codechecker.runners.bash.Bash._check_position')
@patch('cc_codechecker.runners.bash.subprocess.check_output')
def test_version(output: MagicMock, check: MagicMock, bash_runner: Bash):
  """Test the return value of version method."""
  output.return_value = '1.0.0'
  check.return_value = '/usr/bin/bash'
  ver = bash_runner.version()
  assert ver == '1.0.0'

@patch('cc_codechecker.runners.bash.Bash._check_position')
@patch('cc_codechecker.runners.bash.subprocess.run')
def test_run(run: MagicMock, check: MagicMock, bash_runner: Bash):
  """Test the return value of run method."""
  run.return_value = MagicMock(stdout='', returncode=0)
  check.return_value = '/usr/bin/bash'
  ver = bash_runner.run()
  assert ver[0] == 0
  assert ver[1] == ''
