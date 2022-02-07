"""Test Base Runner Exception throws"""

import pytest

# Codechecker
from cc_codechecker.runner import Runner


@pytest.fixture(name='project_runner')
def fixture_project_runner() -> Runner:
  return Runner()

@pytest.mark.parametrize(
  'method',
  ['position',
   'version',
   'run',
  ],
)
def test_position_raise_exception(
  project_runner: Runner,
  method: str,
):
  with pytest.raises(NotImplementedError) as err:
    getattr(project_runner, method)()
  assert err.errisinstance(NotImplementedError)
