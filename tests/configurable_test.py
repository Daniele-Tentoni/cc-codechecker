# SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com
#
# SPDX-License-Identifier: MIT

"""Unit tests for base configurables."""

import pytest

# Codechecker
from cc_codechecker.configurable import Configurable


@pytest.fixture(name='base_configurable')
def fixture_base_configurable() -> Configurable:
  return Configurable()

class VerboseConfigurable(Configurable):

  def __init__(self, **kwargs) -> None:
    super().__init__(**kwargs)

    self.verbose = self._locals.verbose

@pytest.mark.parametrize('value', [True, False])
def test_verbose_value_set(value: bool):
  configurable = VerboseConfigurable(verbose = value)
  assert configurable.verbose == value

def test_repr_nothing(base_configurable: Configurable):
  assert str(base_configurable) == 'Configurable()'

def test_dump_nothing(base_configurable: Configurable):
  assert base_configurable.dump() == {}

class ExampleConfigurable(Configurable):

  def __init__(self, **kwargs) -> None:
    super().__init__(**kwargs)
    self.example = True

@pytest.fixture(name='example_configurable')
def fixture_example_configurable() -> Configurable:
  return ExampleConfigurable()

def test_repr_something(example_configurable: ExampleConfigurable):
  assert str(example_configurable) == 'ExampleConfigurable(example=True)'

def test_dump_something(example_configurable: ExampleConfigurable):
  assert example_configurable.dump() == { 'example': True }
