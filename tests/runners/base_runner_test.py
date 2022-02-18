# SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com
#
# SPDX-License-Identifier: MIT

"""Test Base Runner Exception throws."""

import pytest

# Codechecker
from cc_codechecker.runner import Runner


@pytest.fixture(name='project_runner')
def fixture_project_runner() -> Runner:
  """Provide common Project instance."""
  return Runner()

@pytest.mark.parametrize(
  'method',
  ['position',
   'version',
   'run',
  ],
)
def test_methods_raise_exception(
  project_runner: Runner,
  method: str,
):
  """Test Error raise for each abstract method."""
  with pytest.raises(NotImplementedError) as err:
    getattr(project_runner, method)()
  assert err.errisinstance(NotImplementedError)
