# SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com
#
# SPDX-License-Identifier: MIT

"""Test Yaml Configuration parsing.
"""
# Standard Library
import textwrap

import pytest  # type: ignore
import yaml  # type: ignore

# Codechecker
from cc_codechecker.challenge import Challenge
from cc_codechecker.configuration import Configuration, get_configuration
from cc_codechecker.project import Project


def test_conf_missing_challenges():
  with pytest.raises(ValueError) as v_err:
    Configuration(
      challenges=[],
      projects=[Project('bash')],
    )
  assert 'Expected at least one challenge' in str(v_err.value)

def test_conf_load_missing_challenges():
  yml = 'projects: csharp'
  conf = yaml.full_load(yml)
  with pytest.raises(ValueError) as v_err:
    get_configuration(conf)
  assert 'Necessary at least one challenge' in str(v_err.value)

def test_conf_missing_projects():
  with pytest.raises(ValueError) as v_err:
    Configuration(
      challenges=[Challenge(name='base')],
      projects=[])
  assert 'Expected at least one project' in str(v_err.value)

def test_conf_load_missing_projects():
  yml = 'challenges: [base, advanced]'
  conf = yaml.full_load(yml)
  with pytest.raises(ValueError) as v_err:
    get_configuration(conf)
  assert 'Necessary at least one project' in str(v_err.value)

@pytest.mark.parametrize('configuration', [
  Configuration(
    challenges=[Challenge(name='base')],
    projects=[Project('bash')],
  ),
  Configuration(
    challenges=[
      Challenge(name='base'),
      Challenge(name='advanced'),
    ],
    projects=[
      Project('bash'),
      Project('csharp'),
    ],
  ),
  Configuration(
    challenges=[
      Challenge(name='base'),
      Challenge(name='advanced'),
    ],
    output='out.txt',
    projects=[
      Project('bash'),
      Project('csharp'),
    ],
  ),
])
def test_conf_repr(configuration: Configuration):
  conf_repr: str = configuration.__repr__()
  assert 'Challenge' in conf_repr
  assert 'Configuration' in conf_repr
  assert 'Project' in conf_repr

def test_write_configuration():
  conf = Configuration(
    challenges=[
      Challenge(
        argument='input1.txt',
        result='output1.txt',
        ),
      Challenge(
        argument='input2.txt',
        result='output2.txt',
        ),
      ],
    output='out.txt',
    projects=[Project('bash')],
  )
  doc = yaml.dump(conf.dump())
  yaml_text = textwrap.dedent('''\
    challenges:
    - argument: input1.txt
      result: output1.txt
    - argument: input2.txt
      result: output2.txt
    output: out.txt
    projects:
    - language: bash
    ''')
  assert yaml_text == doc

def test_read_configuration():
  conf = textwrap.dedent('''\
    challenges: base
    projects:
      - language: 'bash'
      - language: 'csharp'
    ''')
  yaml_dict = yaml.full_load(conf)
  assert isinstance(yaml_dict, dict)
  configuration = get_configuration(yaml_dict)
  assert isinstance(configuration.projects, list)
  assert 2 == len(configuration.projects)
  assert 'bash' == configuration.projects[0].language
  assert 'csharp' == configuration.projects[1].language
