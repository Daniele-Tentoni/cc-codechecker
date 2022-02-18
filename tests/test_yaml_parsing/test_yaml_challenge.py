# SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com
#
# SPDX-License-Identifier: MIT

"""Test Yaml Configuration parsing."""
# Standard Library
from textwrap import dedent

import pytest  # type: ignore
import yaml  # type: ignore

# Codechecker
from cc_codechecker.challenge import Challenge, get_challenge


def test_write_challenge():
  challenge = Challenge(
    argument='input.txt',
    result='result.txt',
    )
  doc = yaml.dump(challenge.dump())
  assert dedent('''\
    argument: input.txt
    result: result.txt
    ''') == doc

def test_read_challenge():
  challenge = dedent("""\
    argument: input.txt
    result: output.txt
    """)
  yaml_loaded = yaml.full_load(challenge)
  assert isinstance(yaml_loaded, dict)
  challenge = get_challenge(yaml_loaded)
  print(f'Challenge: {challenge}')
  assert 'input.txt' == challenge.argument
  assert 'output.txt' == challenge.result
  assert 0 == challenge.value

def test_read_full_challenge():
  challenge = dedent("""\
    argument: input.txt
    result: result.txt
    value: 2
    """)
  yaml_loaded = yaml.full_load(challenge)
  assert isinstance(yaml_loaded, dict)
  challenge = get_challenge(yaml_loaded)
  assert 'input.txt' == challenge.argument
  assert 'result.txt' == challenge.result
  assert 2 == challenge.value

@pytest.mark.parametrize('document', [
  """\
  argument: input.txt
  arguments: [1, 2]
  """,
])
def test_invalid_challenge(document: str):
  challenge_doc = dedent(document)
  with pytest.raises(ValueError) as err:
    loaded = yaml.full_load(challenge_doc)
    assert isinstance(loaded, dict)
    get_challenge(loaded)
  assert 'Failed to add challenge' in str(err.value)
