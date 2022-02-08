"""Unit tests for Context."""
# Standard Library
from argparse import Namespace

import pytest

# Codechecker
from cc_codechecker.context import Context


@pytest.fixture(name='context')
def fixture_context() -> Context:
  return Context()

def test_default_verbose_option(context: Context):
  assert not context.options().verbose

def test_get_verbose(context: Context):
  gets = Context.get('verbose', True)
  assert context.options().verbose == gets

def test_get_default():
  defs = Context.get('times', 1)
  assert defs == 1

def test_no_persistance():
  context = Context(Namespace(verbose = True))
  assert context.options().verbose
  del context
  context = Context()
  assert not context.options().verbose
